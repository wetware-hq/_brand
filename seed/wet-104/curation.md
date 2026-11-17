# Curation — the WET-97 seed

WET-97 projected the Wetware theme into four universes in Midjourney. The Midjourney Bot posted the PromptTree to `#media` in the Wetware Discord on 2026-11-15: four branches of four shots each (a cell macro, a neural-lattice wide, a researcher over the shoulder, a humanoid awakening), in the prompt grammar `image · camera · subject · background · director · producer · art · style`.

| Branch | Director / art | Style |
| --- | --- | --- |
| Spider-Verse | Phil Lord & Chris Miller / Alberto Mielgo | halftone, CMYK misregistration, comic ink |
| Edgerunners | Hiroyuki Imaishi / Studio Trigger | saturated neon cel-shading |
| Pluto | Naoki Urasawa / Studio M2 | grounded painterly realism |
| Suzume | Makoto Shinkai / CoMix Wave Films | luminous skies, god-rays |

That makes 16 grids and 64 tiles. Four tiles were kept.

## Kept

| Tile | Branch, shot | Why |
| --- | --- | --- |
| [`mj-03-researcher-tissue-dish`](assets/curated/mj-03-researcher-tissue-dish.jpg) | Spider-Verse, researcher | Someone cradling glowing tissue beside a heartbeat trace: the care and the feeding. It sets the character's mood. |
| [`mj-04-grown-tissue-figure`](assets/curated/mj-04-grown-tissue-figure.jpg) | Spider-Verse, awakening | A body grown from red tissue and fibre. It becomes PROOF's magenta seams. |
| [`mj-01-red-aisle`](assets/curated/mj-01-red-aisle.jpg) | Spider-Verse, wide | A long converging aisle in blood-red light. It becomes the Feed Hall's spine and palette. |
| [`mj-00-first-spark-neuron`](assets/curated/mj-00-first-spark-neuron.jpg) | Spider-Verse, macro | The magenta glow of living tissue in the dark. Also a palette reference. |

`mj-01` and `mj-00` went to Seedream 5.0 Pro as palette-and-light references for the locked Feed Hall plate. The text-only alternate shows what they added. `mj-03` and `mj-04` shaped the writing of the character and the feeding beat, but were not passed to an image model, because they would have dragged in their illustrated faces.

## Rejected

- **Baked-in text** — most Edgerunners and Pluto tiles print fragments of the prompt into the picture.
- **The Edgerunners creature tiles** — a horror creature, not grown tissue.
- **The Suzume branch** — golden-hour skies and warm light break the night-shift world.
- **The Pluto lab and greenhouse plates** — the realism is right, but the palette is grey-green and the tiles carry text.

## Fetching

```bash
python3 scripts/discord_bridge.py download 1571363587849715762 --out seed-grids \
  --author "Midjourney Bot" --match 479f5b9b 8271183d 72bd86d5 64b1a138
```

Each grid is a 2×2 of 1456×816 tiles. The Midjourney job id, tile index and Discord message of every kept tile are in [`manifest.json`](manifest.json).
