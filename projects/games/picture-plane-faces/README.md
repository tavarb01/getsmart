# Picture Plane Faces

A cartoon-face maker built on Scott McCloud's "Big Triangle" (the Picture Plane) from
*Understanding Comics* (1993). Touch a point on the triangle and the app draws a face in
exactly that style.

- **Reality** (bottom left, cyan): resemblance. Shading, eyelids, lines of age, a photo frame at the corner.
- **Language** (bottom right, magenta): iconic abstraction. Fewer, bolder lines until only a smiley
  is left, then the word "FACE".
- **The Picture Plane** (top, yellow): non-iconic abstraction. Features break into circles, squares,
  triangles and bars that are only themselves.

## Run it

Open `index.html` in a browser (works on iPhone too: AirDrop/Files → open, or host it).
Or serve the folder: `python3 -m http.server 8000` and visit http://localhost:8000.

No install, no build, no dependencies (Google Fonts are used when online, with fallbacks offline).

## How the 343 styles work

The triangle is cut into 7 bands along each of its three directions. Those lines make
49 small triangles (7×7), and each small triangle holds 7 snap points (its centre, 3 toward
its corners, 3 toward its edges), so there are 7×7×7 = **343** positions. The style ID shown
is those three base-7 digits (e.g. `455`).

Each snap point has three weights `r + l + p = 1` (how close it is to each corner).
`faceSVG(r, l, p, seed)` turns those weights into drawing parameters: head shape, line weight,
eye size, colour blending, which details fade in or out, and how far features scatter.
The seed is the style number, so the same dot always gives the same face.

## Things to try changing

- `N = 7` in the script: the number of bands per side (7 → 343 styles).
- `describe()`: the style names and captions for each region.
- `PAL`: the colours used near the Picture Plane corner.
- The URL remembers the style (`index.html#s237`), so you can share a specific face.
