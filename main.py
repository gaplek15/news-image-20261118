"""THE WORLD — front page for 18 November 2026.

A single broadsheet page for a single day. The code here is deliberately
boring: it copies the finished front page to the output folder exactly
as drawn, without touching a byte.

What the page carries: the APEC summit opening in Shenzhen, and the QUAD
unveiling a new plan in Manila as Trump landed there — with the first ever
three-way meeting of Trump, Xi and Putin now a day away in Shenzhen.
Ukraine hammered the Kerch bridge for a second day while Russia pounded
bridges near Kyiv. Iran struck an American radar site in Bahrain and
Kuwait shot down a drone of its own. Nvidia reported quarterly revenue of
$115.84 billion, twice the year before, its board said it will not bring
Jensen Huang back as chief executive, and Trump backed Huang's comeback
anyway. MS Dhoni retired from the IPL to mentor Chennai Super Kings.
Cyclone Akvan bore down on Andhra Pradesh, due ashore around 20 November.
Canada and China stretched out their trade deal as Xi met Carney. Britain
sanctioned firms behind Israeli settlements. Apple's services went dark —
iCloud, the App Store. A Russian military plane came down in Siberia,
killing between thirteen and eighteen people. The UN counted at least 372
civilians killed in Ukraine in October, and the Peace Council warned the
Gaza ceasefire was close to collapse.

Run this script and the bundled page lands in the output folder, the
same every time. No network, no clock, no randomness — deterministic
by construction.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    # The harness tells us where the finished entry belongs.
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    source = Path(__file__).resolve().parent / "news.png"
    shutil.copyfile(source, out_dir / "entry.png")


if __name__ == "__main__":
    main()
