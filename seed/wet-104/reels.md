# The reels

Both reels are one Seedance 2.5 generation each: 8 seconds, vertical 9:16, every cut written into the prompt in the director's syntax. Cut times below are measured from the delivered files, not the prompt; the model lands its cuts near the written seconds rather than on them.

## Reel 1 — PROOF (character)

References: `@Image1` the Feed Hall plate, `@Image2` the PROOF sheet. Prompt: [`prompts/reel-1-character.txt`](prompts/reel-1-character.txt).

The beat: total devotion against a hand with a mind of its own. He listens for a heartbeat, hears one, and the cut answers with a deadpan two-step.

| # | Delivered | Shot | Carries |
| --- | --- | --- | --- |
| 1 | 0.00–1.96 s | Top-down on the steel table: the gloved hand creeps toward the red spool with thread on its finger; the bare hand pins it flat | Strangelove's hand, the cantor's red string |
| 2 | 1.96–3.88 s | Close: one finger slides the round sunglasses down; tired, wet, sincere eyes | Psy's shades, Atom's eyes |
| 3 | 3.88–4.88 s | Top-down: one drop of magenta medium falls into the dish of grown tissue | Mouths to feed |
| 4 | 4.88–6.38 s | Close, from below: he listens to the dish through the stethoscope; a tear runs along the jaw seam; one heartbeat thump | *Pluto*'s android who cries |
| 5 | 6.38–8.04 s | Full figure in the aisle: a foot-to-foot hop with wrists crossed out front like reins, face unchanged | Psy, played completely straight |

## Reel 2 — The Feed Hall (environment)

Reference: `@Image1` the Feed Hall plate. Prompt: [`prompts/reel-2-environment.txt`](prompts/reel-2-environment.txt).

The beat: the hall is alive on its night shift and nobody is watching it — until the tissue gives one heartbeat.

| # | Delivered | Shot |
| --- | --- | --- |
| 1 | 0.00–2.04 s | Macro: a drop of magenta medium swells at the tip of a feeding line and falls |
| 2 | 2.04–3.67 s | Low and wide down the empty aisle to the neon heartbeat; a fluorescent tube flickers |
| 3 | 3.67–4.67 s | Looking up: a bag of medium hangs from an old meat hook and sways |
| 4 | 4.67–5.71 s | Through an incubator door: condensation runs down the glass, a bubble rises |
| 5 | 5.71–6.96 s | Floor level: the spool of red suture thread at the drain gutter |
| 6 | 6.96–8.04 s | Top-down on the table: the tissue contracts once, and the ring light pulses with it |

## Iterations

| Round | Result | Change |
| --- | --- | --- |
| Draft v1, one take each (480p) | Reel 1: shot 1 ran 2.8 s, the gloved hand held the stethoscope, and "wrists crossed low" was read as folded arms, so there was no hop. Reel 2: the neon came out as a cross, and the bag had a printed label. | Shot 1 cut to one action. "Only the bare RIGHT hand ever holds the pipette, the sunglasses or the stethoscope." The hop rewritten as foot-to-foot hops with both clogs leaving the tile, "never folded across the chest". The neon "never a cross, never letters". |
| Draft v2, two takes each (480p) | Reel 1: one take hops, the other barely moves. Reel 2: one take keeps all six cuts, the other merged two shots. | Picked `114b29be` and `b2fd4f1c`. |
| Finals (1080p) | Rendered from the approved drafts; the cuts match the drafts frame for frame. | — |

## Sound

- **In the clip** — diegetic only, per the director: incubator hum, fluorescent buzz, glove creak, the drop, the heartbeat thump, the clogs on wet tile, the trolley wheel, the spool.
- **Score (cantor)** — ElevenLabs Music v2, instrumental, written from the song's themes: a solo viola over a felt-piano pulse that beats like a slow heart, strings swelling ([`prompts/score.txt`](prompts/score.txt)). Its peak is aligned to each payoff: Reel 1 starts 0.05 s into the score, and Reel 2 delays it by 0.95 s. No lyric, melody or artist is used or named.
- **Loudness** — the scored reels land at −14.4 and −14.1 LUFS. The clean reels land at −16.5 and −14.6 LUFS: Reel 1's slap and heartbeat cap its gain, and it is left dynamic rather than crushed. All peaks are limited to −1.5 dBFS.

## Assembly

[`scripts/assemble_reels.py`](../../scripts/assemble_reels.py) rebuilds all four files from the Higgsfield masters in [`manifest.json`](manifest.json). It mixes the score under the diegetic sound, normalises loudness, encodes H.264 at CRF 16, and applies one patch: in Reel 2, frames 88–111, the bag label's pseudo-text is softened under a feathered blur.

## Known drifts

- Reel 1, shot 5: the white rubber clogs became wooden platform sandals.
- Reel 2, shot 3: the bag kept the printed label that the plate's bags carry. Its pseudo-text is softened in assembly, so it reads as an unreadable sticker.
