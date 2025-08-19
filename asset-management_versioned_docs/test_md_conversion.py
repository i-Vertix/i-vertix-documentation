import pytest
import pathlib

import md_conversion


def test_overwrite():

    spath = pathlib.Path(__file__)
    spath = spath.parent
    md_conversion.overwrite_files(
        spath / pathlib.Path("itam_overwrite"),
        spath / pathlib.Path("version-10")
        )

