#!/usr/bin/env python3
"""Entry program for the news-image-20261122 make.fun bounty.

The repository holds the finished image as entry.png; this program copies
it, byte for byte, to the output directory the grader provides
(MAKEFUN_OUTPUT_DIR, default /output). It runs with no network and only
the standard library, and every run writes exactly the same bytes.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # The grader runs this program twice and requires identical output;
    # fail loudly rather than hand over a truncated or altered image.
    with open(src, "rb") as f:
        want = f.read()
    with open(dst, "rb") as f:
        got = f.read()
    if got != want:
        print("error: written image differs from entry.png", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
