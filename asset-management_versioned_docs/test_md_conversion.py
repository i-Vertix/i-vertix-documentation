import pytest
import pathlib
import shutil

import md_conversion
import index



class Test():

    spath = pathlib.Path(__file__)
    sdir = spath.parent


    def test_overwrite(self):

        outdir = self.sdir / pathlib.Path("test/version-10")
        outdir.mkdir(parents=True, exist_ok=True)

        md_conversion.overwrite_files(
            self.sdir / pathlib.Path("itam_overwrite"),
            outdir
            )
        shutil.rmtree(outdir)


    def test_parse_title(self):

        fmap = md_conversion.compute_conversion_list(
            self.sdir / pathlib.Path("../glpi_orig/source"), 
            self.sdir / pathlib.Path("version-10"), 
            skip_list=[]
            )

        res = index.parse_titles(fmap)

    