import os
import yaml
import pathlib
from collections import OrderedDict
import json
import subprocess as sb
import argparse
import shutil


def add_header(file_path):

    lines = []
    with open(file_path, "r", encoding="utf8") as fd:
        lines = fd.readlines()
            
    if lines:
        if not (lines[0].startswith('---') or lines[0].startswith(r'\-\--')):
            #with open(file_path, "w", encoding="utf8") as fd:

            module_name = os.path.basename(file_path)
            module_name = module_name[:-3]
            title = module_name.title()

            header = [
                "---\n",
                f"id: {module_name}\n",
                f"title: {title}\n",
                "---\n",
                "\n",
            ]
    
            header.extend(lines)
            with open(file_path, "w", encoding="utf8") as fd:
                fd.writelines(header)

            #print(header)

            
def set_path(root, path):

    curr = root
    for p in pathlib.Path(path).parts[2:]:

        if p.endswith(".md"):
            curr["items"].append(p[:-3])
            break

        if not curr.get(p):
            curr[p] = {
                "id": p,
                "label": p.title(),
                "items": []
            }
        
        curr = curr[p]

    return root


def parse_index(fpath):
    
    lines = []
    with open(fpath, "r", encoding="utf8") as fd:
        lines = fd.readlines()

    start = -1
    end = -1
    for idx, l in enumerate(lines):
        if l.find(".. toctree::") != -1:
            start = idx + 3
            continue

        if start != -1:
            if idx <= start:
                continue
        
        if start != -1:
            if l == "\n":
                end = idx
                break


    lines = lines[start:end]
    lines = [l.strip() for l in lines]
    lines = [l.split("/")[0] for l in lines]

    return lines


def makedir(path):
    dpath = os.path.dirname(path)
    if not os.path.exists(dpath):
        os.makedirs(dpath, exist_ok=True)
    return


def convert_to_md(in_path, out_path):
    print(f"converting {in_path} {out_path}")
    
    makedir(out_path)
    
    sb.call(["pandoc", in_path, "-f",  "rst", "-t", "markdown", "-o", out_path])
    return


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="GLPI doc converter",
        description='What the program does',
        epilog='Text at the bottom of help'
        )

    parser.add_argument("input_dir")
    parser.add_argument("output_dir")

    args = parser.parse_args()

    input_dir = args.input_dir
    output_dir = args.output_dir

    if input_dir[-1] != "/":
        input_dir = f"{input_dir}/"
    
    if output_dir[-1] != "/":
        output_dir = f"{output_dir}/"

    os.makedirs(output_dir, exist_ok=True)


    #copy images
    #static_dir = os.path.join(output_dir, "static")
    static_dir = output_dir
    os.makedirs(static_dir, exist_ok=True)
    
    for root, _, files in os.walk(input_dir):

        png_files = filter(lambda x: x.endswith(".png"), files)
        for f in png_files:
            in_path = os.path.join(root, f)
            rel_path = root.replace(input_dir, "")
            out_path = os.path.join(
                static_dir, rel_path, f
                )
            makedir(out_path)
            shutil.copy(in_path, out_path)


    #copy and convert md files
    acc = {"items": []}
    indexes = {}
    for root, subdirs, files in os.walk(input_dir):

        png_files = filter(lambda x: x.endswith(".png"), files)
        for f in png_files:
            in_path = os.path.join(root, f)
            rel_path = root.replace(input_dir, "")
            out_path = os.path.join(
                static_dir, rel_path, f
                )
            makedir(out_path)
            shutil.copy(in_path, out_path)

        rst_files = filter(lambda x: x.endswith(".rst"), files)
        for f in rst_files:
            
            in_path = os.path.join(root, f)
            out_path = os.path.join(
                root.replace(input_dir, output_dir), 
                f.replace(".rst", ".md")
                )

            if f == "index.rst":
                indexes[in_path] = parse_index(in_path)

            print(in_path, out_path)
            convert_to_md(in_path, out_path)
            
            add_header(out_path)
            
            path_obj = pathlib.Path(out_path)
            set_path(acc, path_obj)



    items = acc.pop("items")
    acc = [v for k, v in acc.items()]
    acc.extend(items)
    acc = {"sidebar" : acc}

    print(yaml.dump(acc, sort_keys=False))
    with open("10-sidebar.yaml.new", "w") as fd:
        fd.write(yaml.dump(acc, sort_keys=False))
