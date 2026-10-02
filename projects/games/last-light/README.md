# Last Light

A playable, real-time 3D storm-coast world for the browser, built for the iPhone first.
You are the keeper of a dying chain of lighthouses and the pilot of a small motor-sailer.
It is one endless grey day and night on a North Atlantic coast. The lamps keep failing.
Sail out, climb the towers, and relight them before the sea takes you.

Single `index.html`, Three.js loaded from a CDN, no build step.

## Run it

- **Desktop:** open `index.html` in a browser, or `python3 -m http.server 8000` in this folder.
- **iPhone, same Wi-Fi:** run `python3 -m http.server 8000` on your computer, then open
  `http://<your-computer's-IP>:8000` in Safari. Tap Share → *Add to Home Screen* for a full-screen,
  no-toolbar launch. Turn the sound on with the **SND** button (iOS only allows audio after a tap).
- **Anywhere:** push the folder to GitHub Pages (or any static host) and open the URL on the phone.

Add `?fps=1` to the URL for a small fps / resolution readout. The game lowers its render
resolution automatically if the phone can't hold ~45 fps. Add `?skip=1` to skip the intro.

## Controls (touch)

| Do this | To do that |
| --- | --- |
| Drag on the **left** half | Virtual stick: left/right = rudder, up = throttle (it stays set when you let go), down = cut / reverse |
| Drag on the **right** half | Orbit the camera |
| **SAIL** | Cycle sail: off → reefed → full. Reef when the wind rises or you'll roll over |
| **VIEW** | Chase / under the sea / bow |
| **CLIMB / DOCK / RESCUE** | Appears near a tower, the harbour, or a vessel in distress. Hold it |
| **PHOTO** | Free-fly camera, time frozen. Left stick moves, right half looks, UP/DOWN/FAST |
| **SND** | Mute |

Desktop: `W/S` throttle, `A/D` rudder, `Space` hold-to-act, `F` sail, `V` view, `P` photo, mouse-drag to look.

## How to play

- The row of dots top-left is your lighthouses (● lit, ○ dark). All dark for 6 seconds and it's over.
- The compass strip shows bearings to every lamp (filled = burning), the harbour (□) and any distress flare (!).
  In fog and at night this is how you find things.
- Each lamp burns down faster in a gale and can be blown out. Relighting costs one fuel can.
  The harbour refuels the boat, patches the hull, restocks cans, and warms you up.
- Watch **HULL**, **FUEL** and **WARM**. Wet, windy exposure drains warmth; rocks and slamming into
  waves damage the hull; sitting beam-on to big breaking seas can capsize you.
- At night, a red flare means someone is out there. Reach them within about two and a half minutes.

## How it works

- **Ocean:** six Gerstner wave trains (wavelengths 7–140 m) summed in the vertex shader and re-evaluated
  per pixel for normals. The *same* wave function runs on the CPU, so the boat, buoys, foam and spray sit
  on the real surface. Sea state (0–1) scales the amplitudes; wind and weather drive it.
- **Foam:** from the Jacobian of the wave displacement (where crests pinch together), broken up with noise
  into lace and wind-aligned streaks, plus wake and shoreline foam patches that fade over time.
- **Sky:** one shader gives sky, cloud deck, stars and moon; the same sky function is reflected by the
  water, so the sea always matches the light overhead. Lighthouse lamps, the boat lamp and the moon add
  glitter to the water.
- **Time:** the simulation uses a fixed 1/60 s step with a catch-up cap, so a dropped frame or a tab
  switch can't blow up the physics or the splashes.
- **Honest limits:** this is a Gerstner sum, not a full FFT ocean. There is no screen-space reflection or
  real cloud shadow on the water (a noise stand-in darkens patches). The lighthouse climb is a progress bar, not a
  first-person walk. Sound is synthesised, not recorded.
