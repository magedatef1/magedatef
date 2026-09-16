from pathlib import Path


MEDIA_DIR = Path("storage/media")
UPLOAD_DIR = Path("storage/uploads")

MEDIA_DIR.mkdir(
    parents=True,
    exist_ok=True
)

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True
)
