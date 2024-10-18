# Copyright (C) 2024 Travis Abendshien (CyanVoxel).
# Licensed under the GPL-3.0 License.
# Created for TagStudio: https://github.com/CyanVoxel/TagStudio

import io
from pathlib import Path

import pytest
from PIL import Image
from src.qt.widgets.thumb_renderer import ThumbRenderer
from syrupy.extensions.image import PNGImageSnapshotExtension


@pytest.mark.parametrize(
    ["fixture_file", "thumbnailer"],
    [
        (
            "sample.odt",
            ThumbRenderer._open_doc_thumb,
        ),
        (
            "sample.ods",
            ThumbRenderer._open_doc_thumb,
        ),
    ],
)
def test_document_preview(cwd, fixture_file, thumbnailer, snapshot):
    file_path: Path = cwd / "fixtures" / fixture_file
    img: Image.Image = thumbnailer(file_path)

    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)
    assert img_bytes.read() == snapshot(extension_class=PNGImageSnapshotExtension)
