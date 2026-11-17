# WET-104 — Seed reel: Wetware

Two 8-second vertical reels that seed the core aesthetic of Wetware: one for the character, one for the environment. They were made on Higgsfield, written in the cloned syntax of the director joeysnoisygroup, tasted with *Mouths to Feed* (zeitgeist) and *the cure* (cantor), and seeded from the WET-97 Midjourney projection that lives in the Wetware Discord.

## The reels

| Reel | File | Shots | What it shows |
| --- | --- | --- | --- |
| 1 — PROOF (character) | [`reels/wet-104-reel-1-character.mp4`](reels/wet-104-reel-1-character.mp4) | 5 | An android doctor on the 3 a.m. feeding round. His gloved hand has a mind of its own; he listens to a dish of grown tissue, hears a heartbeat, and answers with a deadpan two-step. |
| 2 — The Feed Hall (environment) | [`reels/wet-104-reel-2-environment.mp4`](reels/wet-104-reel-2-environment.mp4) | 6 | The empty hall alive on its night shift — a drop, a flicker, a hook, condensation, a rolling spool of red thread — until the tissue gives one heartbeat. |

Both are 1080×1920, 24 fps, H.264 with AAC, mixed to −14 LUFS. The `-clean` files carry the diegetic sound only, for posting under a licensed track.

## How it was made

1. **Curate** — 4 of the 64 WET-97 Midjourney tiles were kept as the seed ([`curation.md`](curation.md)).
2. **Clone** — the director's suite, taste and prompt syntax were read from his public Higgsfield film and written down as an identity ([`identity.md`](identity.md)).
3. **Lock the environment** — the Feed Hall as an empty plate, with the curated palette passed as a reference ([`environment.md`](environment.md)).
4. **Lock the character** — PROOF, from the role-model mix, as a casting photo and then a three-panel sheet ([`character.md`](character.md)).
5. **Shoot** — Seedance 2.5 drafts at 480p, two rounds, then the approved takes finalised at 1080p ([`reels.md`](reels.md)).
6. **Assemble** — an original score laid under the diegetic sound, one patch of pseudo-text softened, loudness normalised.

## Taste inputs

- **Zeitgeist — [*Mouths to Feed*](https://www.backerkit.com/c/projects/tuesday-knight-games/mouths-to-feed)** (Mothership: Prospero's Dream). A company tower built on a slaughterfactory, famine and faith, Slickware Magenta. In Wetware the cultures are the mouths to feed, and the slaughter floor has become a tissue farm.
- **Cantor — [*the cure*](https://genius.com/Olivia-rodrigo-the-cure-lyrics)**. Antidote and poison in the bloodstream, a medication that is not a cure, coming unravelled, a red string, strings that swell. In the reels: red suture thread, a tear, a heartbeat, a solo-viola score. No lyric, melody or recording of the song is used.
- **Reference art (WET-97)** — the humane androids of *Pluto* lead the character; *Into the Spider-Verse* and *Edgerunners* survive as the palette of the curated seed.

## Contents

| Path | What |
| --- | --- |
| [`identity.md`](identity.md) | The cloned directorial suite: identity, taste, syntax |
| [`curation.md`](curation.md) | Which WET-97 tiles were kept, which were rejected, and why |
| [`character.md`](character.md) | PROOF: the role-model mix, the locks, how he was made |
| [`environment.md`](environment.md) | The Feed Hall: sources and locked landmarks |
| [`reels.md`](reels.md) | Shot lists as delivered, iterations, sound, known drifts |
| [`launch.md`](launch.md) | Launch lines for the event announcement (WET-104 comment dc0fdbad) |
| [`incept.md`](incept.md) | Vague teaser posts, one incepted per launch post |
| [`manifest.json`](manifest.json) | Every source, Higgsfield job, decision, and credit |
| [`prompts/`](prompts) | The exact prompts sent |
| [`assets/`](assets) | Curated tiles, location plates, casting photo, character sheet |

## Reproduce

```bash
python3 scripts/assemble_reels.py           # rebuild reels/ from the Higgsfield masters in manifest.json
python3 scripts/discord_bridge.py whoami    # the WET-102 bridge used to pull the seed and post the reels
```

The bridge reads the bot token from `DISCORD_BOT_TOKEN` (or `discord_agent_token`); nothing else is needed. Assembly needs `ffmpeg`.

## Spend

436.68 of 1,200 Higgsfield credits: 35 on stills, 144 on six drafts, 256 on two 1080p finals, 1.68 on the score.
