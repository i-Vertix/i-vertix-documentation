import os
import sys
import yaml
import pathlib
from collections import OrderedDict
import json


def add_header(file_path):

    lines = []
    with open(file_path, "r", encoding="utf8") as fd:
        lines = fd.readlines()
            
    if lines:
        if not lines[0].startswith('---'):
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



if __name__ == "__main__":

    acc = {"items": []}
    for root, subdirs, files in os.walk(sys.argv[1]):

        files = filter(lambda x: x.endswith(".md"), files)
        for f in files:
            
            path = os.path.join(root, f)

            if f == "index.md":
                parse_index(path)

            add_header(path)

            path = pathlib.Path(path)
            set_path(acc, path)

    items = acc.pop("items")
    acc = [v for k, v in acc.items()]
    acc.extend(items)
    acc = {"sidebar" : acc}

    #print(yaml.dump(acc, sort_keys=False))
