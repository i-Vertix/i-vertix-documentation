import os
import yaml
import pathlib
from collections import OrderedDict
import json
import subprocess as sb
import argparse
import shutil
import re

yaml.add_representer(OrderedDict, lambda dumper, data: dumper.represent_mapping('tag:yaml.org,2002:map', data.items()))

def dump_struct(s):
    print(json.dumps(s, indent=4))
    return


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
    for p in pathlib.Path(path).parts:

        items = curr["items"]

        if p.endswith(".md"):
            curr["items"].append(p[:-3])
            break

        pres = [e for e in items if isinstance(e, dict) and e["id"] == p]
        if not pres:
            next_elem = {
                "id": p,
                "label": p.title(),
                "items": []
            }
            items.append(next_elem)
        else:
            next_elem = pres[0]
        
        curr = next_elem

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

    #No index list present
    if start == -1:
        return []

    #If file ends just after the index
    if end == -1: 
        end = len(lines)

    lines = lines[start:end]
    lines = [l.strip() for l in lines]
    lines = [l.split("/")[0] for l in lines]
    lines.insert(0, "index")

    return lines


def makedir(path):
    dpath = os.path.dirname(path)
    if not os.path.exists(dpath):
        os.makedirs(dpath, exist_ok=True)
    return


def convert_to_md(in_path, out_path):
    print(f"converting {in_path} {out_path}")
    
    makedir(out_path)
    
    #sb.call(["pandoc", in_path, "-f",  "rst", "-t", "markdown_strict", "-o", out_path])
    sb.call(["pandoc", in_path, "-f",  "rst", "-t", "markdown", "-o", out_path])
    return


def sort_index_tree(tree, indexes):
    
    def ordered_dict_rec(tree, indexes=indexes, cpath=[]):

        if isinstance(tree, dict):

            newl = list(cpath)
            newl.append(tree["id"])

            return OrderedDict([
                ("id", tree["id"]),
                ("label", tree["label"]),
                ("items", ordered_dict_rec(
                    tree["items"], 
                    indexes,
                    newl
                    )
                )
            ]
            )
        elif isinstance(tree, list):
            
            res = [ordered_dict_rec(x, indexes, cpath) for x in tree]

            def sorter(x): 
                index = indexes.get(tuple(cpath), [])

                if isinstance(x, OrderedDict):
                    x = x["id"]
                
                #print(f"sorter {cpath} {x} {index}")

                if x in index:
                    return index.index(x)
                
                return len(index)

            res = sorted(res, key=sorter)
            return res
        
        elif isinstance(tree, str):
            return tree

    #for i in indexes:
    #    print(f"\"{i}\" -> {indexes[i]}")

    tree = ordered_dict_rec(tree)
    #print(json.dumps(tree, indent=4))

    return tree


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
    out_files = []
    for root, subdirs, files in os.walk(input_dir):
            
        rst_files = filter(lambda x: x.endswith(".rst"), files)
        for f in rst_files:
            
            out_file = f.replace(".rst", ".md")
            
            in_path = os.path.join(root, f)
        
            rel_dir = root.replace(input_dir, "")
            rel_path = os.path.join(rel_dir, out_file)
            
            out_dir = root.replace(input_dir, output_dir)
            out_path = os.path.join(out_dir, out_file)
            out_files.append(out_path)

            if f == "index.rst":
                index_path = tuple(pathlib.Path(rel_dir).parts)
                indexes[index_path] = parse_index(in_path)

            #print(in_path, out_path)
            convert_to_md(in_path, out_path)
            add_header(out_path)
            set_path(acc, pathlib.Path(rel_path))



    items = acc.pop("items")
    acc = [v for k, v in acc.items()]
    acc.extend(items)
    acc = sort_index_tree(acc, indexes)
    acc = {"sidebar" : acc}
    
    #print(yaml.dump(acc, sort_keys=False))
    with open("itam_versioned_sidebars/10-sidebar.yaml", "w") as fd:
        fd.write(yaml.dump(acc, sort_keys=False))

    
    # parse / copy all common images
    static_dir = os.path.join(output_dir, "static")
    os.makedirs(static_dir, exist_ok=True)
    common_images = []
    for f in out_files:

        lines = []
        with open(f, "r", encoding="utf8") as fd:
            lines = fd.readlines()

        for l in lines:
            img_include = re.match(r"!\[([\w ]+)\]\(([\w\/\. ]+)\)", l)
            if img_include:
                img = img_include.group(2)
                if img.startswith("/"):
                    common_images.append(img_include.group(2))

    common_images = list(set(common_images))
    print(len(common_images))
    for c in common_images:
        in_path = os.path.join(input_dir, c[1:])
        out_path = os.path.join(static_dir, c[1:])
        makedir(out_path)
        shutil.copy(in_path, out_path)
        #print(c)

    


    for f in out_files:

        text = ""
        with open(f, "r", encoding="utf8") as fd:
            text = fd.read()

        match = re.search(r":::: ([\w]+)\s*::: title\s*(.*?)\s*:::\s*(.*?)::::\s*", text, re.DOTALL)
        if match:
            new_text = f":::{match.group(1)}\n{match.group(3)}\n:::\n\n"
            text = text[:match.start()] + new_text + text[match.end():]

        with open(f, "w", encoding="utf8") as fd:
            fd.write(text)
    
    
    #for f in out_files:

    #    lines = []
    #    with open(f, "r", encoding="utf8") as fd:
    #        lines = fd.readlines()

    #    #with open(f, "w", encoding="utf8") as fd:
    #    #    fd.writelines(lines)