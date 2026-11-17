#!/usr/bin/env python3
"""Bridge between cloud agents and the Wetware Discord server (WET-102).

Uses the agent bot token only, read from DISCORD_BOT_TOKEN or discord_agent_token.

  discord_bridge.py whoami
  discord_bridge.py history CHANNEL [--limit N] [--out FILE]
  discord_bridge.py download CHANNEL --out DIR [--author NAME] [--match TEXT ...]
  discord_bridge.py post CHANNEL [--text TEXT] [--file PATH ...] [--thread NAME]
"""

import argparse
import json
import mimetypes
import os
import sys
import time
import urllib.error
import urllib.request
import uuid

API = "https://discord.com/api/v10"
USER_AGENT = "DiscordBot (https://github.com/wetware-hq/_brand, 1.0)"
MAX_FILES_PER_MESSAGE = 10


def token():
    value = os.environ.get("DISCORD_BOT_TOKEN") or os.environ.get("discord_agent_token")
    if not value:
        sys.exit("Set DISCORD_BOT_TOKEN (or discord_agent_token) to the agent bot token.")
    return value.strip()


def request(method, path, body=None, content_type="application/json"):
    headers = {"Authorization": "Bot " + token(), "User-Agent": USER_AGENT}
    data = None
    if body is not None:
        data = body if isinstance(body, bytes) else json.dumps(body).encode()
        headers["Content-Type"] = content_type
    while True:
        req = urllib.request.Request(API + path, data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                raw = resp.read()
                return json.loads(raw) if raw else None
        except urllib.error.HTTPError as err:
            if err.code == 429:
                time.sleep(float(json.loads(err.read() or b"{}").get("retry_after", 1.0)) + 0.1)
                continue
            sys.exit(f"Discord {method} {path} failed: {err.code} {err.read()[:300].decode(errors='replace')}")


def history(channel, limit=None):
    messages, before = [], None
    while limit is None or len(messages) < limit:
        page_size = 100 if limit is None else min(100, limit - len(messages))
        query = f"?limit={page_size}" + (f"&before={before}" if before else "")
        page = request("GET", f"/channels/{channel}/messages{query}")
        messages += page
        if len(page) < page_size:
            break
        before = page[-1]["id"]
    return list(reversed(messages))


def multipart(payload, paths):
    boundary = uuid.uuid4().hex
    parts = [
        f"--{boundary}\r\nContent-Disposition: form-data; name=\"payload_json\"\r\n"
        f"Content-Type: application/json\r\n\r\n{json.dumps(payload)}\r\n".encode()
    ]
    for index, path in enumerate(paths):
        name = os.path.basename(path)
        mime = mimetypes.guess_type(name)[0] or "application/octet-stream"
        with open(path, "rb") as handle:
            content = handle.read()
        parts.append(
            f"--{boundary}\r\nContent-Disposition: form-data; name=\"files[{index}]\"; filename=\"{name}\"\r\n"
            f"Content-Type: {mime}\r\n\r\n".encode() + content + b"\r\n"
        )
    parts.append(f"--{boundary}--\r\n".encode())
    return b"".join(parts), f"multipart/form-data; boundary={boundary}"


def post(channel, text=None, paths=(), thread=None):
    paths = list(paths)
    first_batch, rest = paths[:MAX_FILES_PER_MESSAGE], paths[MAX_FILES_PER_MESSAGE:]
    payload = {"content": text or "", "allowed_mentions": {"parse": []}}
    body, content_type = multipart(payload, first_batch)
    message = request("POST", f"/channels/{channel}/messages", body, content_type)
    target = channel
    if thread:
        created = request("POST", f"/channels/{channel}/messages/{message['id']}/threads",
                          {"name": thread[:100], "auto_archive_duration": 10080})
        target = created["id"]
    while rest:
        batch, rest = rest[:MAX_FILES_PER_MESSAGE], rest[MAX_FILES_PER_MESSAGE:]
        body, content_type = multipart({"content": "", "allowed_mentions": {"parse": []}}, batch)
        request("POST", f"/channels/{target}/messages", body, content_type)
    return message, target


def cmd_whoami(_):
    me = request("GET", "/users/@me")
    print(f"{me['username']} ({me['id']})")
    for guild in request("GET", "/users/@me/guilds"):
        print(f"guild {guild['id']} {guild['name']}")
        for channel in request("GET", f"/guilds/{guild['id']}/channels"):
            print(f"  channel {channel['id']} type={channel['type']} #{channel['name']}")


def cmd_history(args):
    messages = history(args.channel, args.limit)
    if args.out:
        with open(args.out, "w") as handle:
            json.dump(messages, handle, indent=1)
    for message in messages:
        files = ", ".join(a["filename"] for a in message.get("attachments", []))
        text = (message.get("content") or "").replace("\n", " ")[:160]
        print(f"{message['id']} {message['timestamp'][:19]} {message['author']['username']}: {text} [{files}]")


def cmd_download(args):
    os.makedirs(args.out, exist_ok=True)
    for message in history(args.channel):
        if args.author and message["author"]["username"] != args.author:
            continue
        content = message.get("content") or ""
        if args.match and not any(m in content for m in args.match):
            continue
        for attachment in message.get("attachments", []):
            target = os.path.join(args.out, f"{message['id']}_{attachment['filename']}")
            req = urllib.request.Request(attachment["url"], headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=120) as resp, open(target, "wb") as handle:
                handle.write(resp.read())
            print(target)


def cmd_post(args):
    message, target = post(args.channel, args.text, args.file, args.thread)
    print(json.dumps({"message": message["id"], "channel": target}))


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("whoami").set_defaults(func=cmd_whoami)
    p = sub.add_parser("history")
    p.add_argument("channel")
    p.add_argument("--limit", type=int)
    p.add_argument("--out")
    p.set_defaults(func=cmd_history)
    p = sub.add_parser("download")
    p.add_argument("channel")
    p.add_argument("--out", required=True)
    p.add_argument("--author")
    p.add_argument("--match", nargs="*")
    p.set_defaults(func=cmd_download)
    p = sub.add_parser("post")
    p.add_argument("channel")
    p.add_argument("--text")
    p.add_argument("--file", nargs="*", default=[])
    p.add_argument("--thread")
    p.set_defaults(func=cmd_post)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
