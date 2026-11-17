# Identity — cloned directorial suite

`clone-directorial-suite`: MODE Expert Forger, DEGREE Linguistics, TARGET Film Director, FOR EACH Asset CLONE Syntax, RETURN Identity --Taste --Style.

| | |
| --- | --- |
| Director | [joeysnoisygroup](https://higgsfield.ai/@joeysnoisygroup) — Higgsfield Creative Partner, "building the CTRL WORLD in public" |
| Film (FP) | [EVERYTHING NICE HAPPENS WHEN I SLEEP](https://higgsfield.ai/@joeysnoisygroup/projects/everything-nice-happens-when-i-sleep) — 72.9 s, 3840×2160, published 2026-08-20 with prompts shown |
| Assets read | 16 (15 generations + 1 upload) across three folders |
| Stack | Seedance 2.5 47% · Nano Banana Pro 27% · Seedream 5.0 Pro 13% · Cinema Studio 4.0 7% · Cinematic Studio 7% |
| Spend | 995 credits |

## Identity

The suite is three folders, built in this order:

1. **Location Locks** — an empty, very wide plate of the one room (text only, Seedream 5.0 Pro), then staged plates of a character inside it.
2. **Characters + Props** — a full-length casting photo on 18% grey, a three-panel sheet made *from* that casting photo, and props shot alone on the same grey.
3. **Video Gens** — multi-shot Seedance 2.5 clips with hard cuts written into one prompt, every person, prop and the room passed as a reference.

Nothing is generated in a clip that was not locked as an asset first.

## Taste

- **The cut is the joke.** "The comedy lives entirely in the collision of the two shots and never inside either one." Each shot is played completely sincere; the meaning is in the edit.
- **Ordinary people, absurd situation, Tuesday-errand energy.** A woman in a mascot suit doing her laundry is treated as routine. Nobody mugs, nobody double-takes.
- **Clothes that do not fit the body.** The gorilla suit is "built for a body roughly twice her size" — the silhouette carries the character.
- **Empty after-hours rooms.** "Nobody else is in the frame" is a critical rule in every clip; reflections are policed too.
- **One practical light plus one saturated neon.** Yellowed fluorescent panels overhead, pink neon in the window, lifted blacks, low macro contrast, high micro contrast.
- **Real time and real sound.** No slow motion, no ramping, true 180° shutter, diegetic audio only, no music.

## Style — the syntax

### Image grammar (casting, sheets, props)

1. One framing sentence: what the image is and how it is composed ("A three-panel character reference sheet composed as one horizontal frame…").
2. The body, then the face, hair, makeup and nails, then the wardrobe head to toe — every item with material, cut, colour and wear.
3. Panel blocks in capitals: `LEFT PANEL —`, `CENTER PANEL —`, `RIGHT PANEL —` (full body front, full body rear or variant, chest-up face lock).
4. A skin-tone lock sentence ("never cool-shifted, never pale…").
5. The background lock: "a single flat 18% neutral gray field — one uniform value at every pixel corner to corner…".
6. "Relight from scratch…" — flat, shadowless, catalogue light.
7. "Absolutely zero shadow anywhere outside the subject…".
8. A materials-realism list ending "never plastic-looking in the CGI sense".
9. The optics close: "Even sharpness edge to edge… Photographed on a 50mm prime, soft natural film grain. Photographed not generated."

### Location-lock grammar (plates)

1. Opener: "A cinematic anamorphic still photograph captured handheld on a real cinema set — a very wide deep-perspective interior composition of a completely empty …", ending on "nobody anywhere in the frame and no figures, silhouettes, or reflections of people in any surface."
2. "… are the spine of the composition" — the repeating element in converging perspective.
3. The room: surfaces, wear, floor.
4. The one sign or neon, and how its colour falls off.
5. Light and air: "Every lit source in the frame carries real optical bloom and refraction…", "The air carries continuous light scattering from the lens all the way to the back wall with no exemption in the near field…".
6. Capture: "wide-latitude cinema look and a vintage 40mm-equivalent 2x anamorphic character at a wide aperture… color-negative tungsten film rendition, in an M1 cinematic narrative register", heavy 35mm grain, a balanced grade.
7. Realism close: "Real photographic frame captured on a real cinema camera… — no CGI, no rendered look…".

### Video grammar (Seedance 2.5)

Always in this order:

1. **Shot clock** — "N shots. Total X seconds — shot 1 runs a–b s … Hard cuts between them, no transitions, no dissolves. All shots real-time…".
2. **Style / Operating style / Texture / Skin / Technical** — photoreal large-format film, handheld intimacy, 24 fps, 1/48 s shutter.
3. **CRITICAL blocks** — `NO ON-SCREEN TEXT`, `THE BEAT`, `NOBODY ELSE IS IN THE FRAME`, plus one block per risk (`THE SNEEZE`, `THE BITE IS REAL`, `THE SUIT IS A COSTUME`). Each says what must happen, then lists every "never".
4. **ASSETS** — each reference as `<<<element>>> = description. THIS SCENE: … 100% match to the reference.`; incidental subjects as `@name = …`; the room "Controls materials, atmosphere and light direction only."
5. **GEOMETRY MAP** — positions, screen direction, depth planes.
6. **FIRST FRAME** — the action is already underway; never an empty establishing frame.
7. **LENS LOCK SHOT n** — field of view in degrees with the focal length ("18° (105mm) portrait tight…").
8. **CAMERA**, **LIGHT**, **COLOUR** (as percentages of the frame), **ATMOSPHERE**.
9. **ACTION TIMING** — beats by the second, with a `HARD CUT` line at every cut.
10. **PHYSICS**, **ACTING**, **AUDIO** ("diegetic only … No music, no lyrics, no score").
11. **LOCKS** — order of events, identity, wardrobe, light, texture.

## How WET-104 applies it

| Kept verbatim | Changed for Wetware |
| --- | --- |
| Three-folder build order; casting photo → sheet; empty location lock | The room is a cell-culture feed hall in an old abattoir, not a laundromat |
| 18% grey sheet, flat relight, zero-shadow and optics clauses | Palette comes from the curated WET-97 seed: magenta tissue-glow against cold fluorescent |
| Shot clock, CRITICAL blocks, ASSETS, GEOMETRY MAP, FIRST FRAME, LENS LOCKs, COLOUR percentages, ACTION TIMING, LOCKS | References are `@Image1…n` (the MCP's Seedance convention) instead of `<<<element-id>>>` |
| Deadpan sincerity, nobody else in frame, diegetic sound in the clip | Fast cuts: five or six shots in 8 s (1.3–2.1 s each) instead of 3–4 s shots |
| Costume built for a body twice the size | The cantor's score is laid under the clip at assembly, instrumental only |
