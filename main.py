"""Make.fun entry: Sum up 24 November's world news in one image.

Copies the front-page image the repository holds to /output/entry.png.
The image is deterministic: the same bytes are written on every run.
"""
import pathlib
import shutil

SRC = pathlib.Path(__file__).with_name("entry.png")
OUT = pathlib.Path("/output/entry.png")

def main():
    # Gate: the image must be a PNG of at most 1 MiB and 1024x1024.
    data = SRC.read_bytes()
    assert data[:8] == b"\x89PNG\r\n\x1a\n", "entry.png is not a PNG"
    assert len(data) <= 1048576, len(data)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)

if __name__ == "__main__":
    main()
