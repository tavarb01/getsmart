# Picture Plane Faces

A cartoon-face maker built on Scott McCloud's "Big Triangle" (the Picture Plane) from
*Understanding Comics* (1993). Touch a point on the triangle and the app draws a face in
exactly that style.

- **Reality** (bottom left, cyan): resemblance. Shading, eyelids, lines of age, a photo frame at the corner.
- **Language** (bottom right, magenta): iconic abstraction. Fewer, bolder lines until only a smiley
  is left, then the word "FACE".
- **The Picture Plane** (top, yellow): non-iconic abstraction. Features break into circles, squares,
  triangles and bars that are only themselves.

## Modes (the round 0 / 1 / 2 dial)

- **Mode 0: Generated face.** Code draws an original face for each of the 343 positions.
- **Mode 1: McCloud's canon (7×7 starter).** Like McCloud's own chart, each of the 49 small triangles
  holds a famous cartoon character (e.g. *Kenny McCormick by Trey Parker & Matt Stone*,
  *Popeye by E. C. Segar*). The picture and the creator's photo load live from Wikipedia. The
  placements are an approximation in the spirit of McCloud's chart, not a copy of it. Edit
  `CANON_ROWS` in the script to move or swap characters (row 0 = top, left = Reality).
  If a picture can't load, a generated face in that cell's style is shown instead, labelled "stand-in".
- **Mode 2: AI prompts.** One image-generator prompt for every one of the 343 positions. Copy one,
  or copy all 343 as JSON. The same list is saved in `prompts-343.json`. Every prompt ends with a separate line `Ref 452 (...do not draw it)`,
  so you can send a generated picture back with its ID. The "Have an ID?" box jumps to any ID.
  `GEMINI_PROMPTS.md` has everything for Gemini in one file: the setup message, a test batch, a correction
  message and all 49 batches of 7. The prompts describe the
  style position and don't name real characters or artists, so the results are original faces.

## Run it

Open `index.html` in a browser (works on iPhone too: AirDrop/Files → open, or host it).
Or serve the folder: `python3 -m http.server 8000` and visit http://localhost:8000.

**On iPhone with the Mode 1 pictures:** open
https://raw.githack.com/tavarb01/getsmart/claude/picture-plane-faces/projects/games/picture-plane-faces/index.html
(the Claude artifact preview blocks outside images, so there Mode 1 shows stand-ins).

No install, no build, no dependencies (Google Fonts are used when online, with fallbacks offline).

## How the 343 styles work

The triangle is cut into 7 bands along each of its three directions. Those lines make
49 small triangles (7×7), and each small triangle holds 7 snap points (its centre, 3 toward
its corners, 3 toward its edges), so there are 7×7×7 = **343** positions. The style ID shown
is three digits from 1 to 7, so it runs from `111` to `777` (e.g. `452`): the first two digits pick
the small triangle (counted top to bottom, left to right) and the third picks one of its 7 points.

Each snap point has three weights `r + l + p = 1` (how close it is to each corner).
`faceSVG(r, l, p, seed)` turns those weights into drawing parameters: head shape, line weight,
eye size, colour blending, which details fade in or out, and how far features scatter.
The seed is the style number, so the same dot always gives the same face.

## Things to try changing

- `N = 7` in the script: the number of bands per side (7 → 343 styles).
- `describe()`: the style names and captions for each region.
- `PAL`: the colours used near the Picture Plane corner.
- The URL remembers the style (`index.html#s237`), so you can share a specific face.
