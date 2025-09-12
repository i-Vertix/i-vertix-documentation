import os
import pathlib
import json
import subprocess as sb
import argparse
import shutil
import re
from functools import partial
from collections import namedtuple

import index 
import images
import utils


ImgInclude = namedtuple("ImgInclude", "root, inc, path")


def compute_images_list(input_dir):
    """
    """

    pngs = []
    links = {}
    for root, _, files in input_dir.walk():
        
        png_list = filter(lambda x: x.endswith(".png"), files)
        png_list = [ root / p for p in png_list]
        pngs.extend(png_list)

        rst_list = filter(lambda x: x.endswith(".rst"), files)
        for r in rst_list:
            with open(root / r, "r", encoding="utf8") as fd:
                text = fd.read()
                for match in re.finditer(r"\.\. image:: (.*)", text):
                    img_path = pathlib.Path(match.group(1))
                    links[img_path] = ImgInclude(root, match.group(1), img_path)

    #links = [ pathlib.Path(l) for l in links ]
    #for l in links:
    #    print(f"{l} -> {links[l]}")

    missing_imgs = filter(lambda x: not (x.root / x.inc).exists(), links.values())

    # given 2 paths,
    # returns the number of matching path components from the end
    def count_common(la: pathlib.Path, lb: pathlib.Path):

        for idx, (a, b) in enumerate(zip(la.parts[::-1], lb.parts[::-1])):
            if a != b:
                return idx

        return min(len(la.parts), len(lb.parts))

    resolved = {}
    for i in missing_imgs:
        most_matching_path = sorted(pngs, key=partial(count_common, i.path), reverse=True)[0]
        resolved[i.inc] = ImgInclude(i.root, i.inc, most_matching_path)

    links = links | resolved

    #print(len(links))
    #for l in links:
    #    print(l, links[l])

    return pngs, links


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="GLPI doc converter",
        description='What the program does',
        epilog='Text at the bottom of help'
        )

    parser.add_argument("input_dir")
    parser.add_argument("output_dir")
    parser.add_argument("--tmp-dir", default="images_tmp", dest="tmp_dir")
    args = parser.parse_args()

    input_dir = pathlib.Path(args.input_dir)
    output_dir = pathlib.Path(args.output_dir)
    tmp_dir = pathlib.Path(args.tmp_dir)

    output_dir.mkdir(exist_ok=True)
    
    # copy tmp dir    
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)

    shutil.copytree(input_dir, tmp_dir)
    input_dir = tmp_dir

    # compute the list of (input, red_dir, output) that will be used in all
    # following ops
    #fmap = compute_conversion_list(input_dir, output_dir)

    images, img_links = compute_images_list(input_dir)

    #print(len(img_links))
    #for l in img_links:
    #    print(l)

    #for i in images:
    #    print(i)
   