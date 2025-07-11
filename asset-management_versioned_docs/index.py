import yaml
import pathlib
from collections import OrderedDict
import re

yaml.add_representer(OrderedDict, lambda dumper, data: dumper.represent_mapping('tag:yaml.org,2002:map', data.items()))

def set_path(root, path):

    curr = root
    for p in path.parts:

        items = curr["items"]

        if p.endswith(".md"):
            curr["items"].append(p[:-3])
            break

        pres = [e for e in items if isinstance(e, dict) and e["id"] == p]
        if not pres:
            next_elem = {
                "id": p,
                "label": p.title().replace("_", " ").replace("-", " "),
                "items": []
            }
            items.append(next_elem)
        else:
            next_elem = pres[0]
        
        curr = next_elem

    return root


def parse_index(fpath):
    
    text = None
    #print(fpath)
    with open(fpath, "r", encoding="utf8") as fd:
        text = fd.read()

    text = text + "\n\n"
    match = re.search(r"\.\. toctree::\n\s+:maxdepth: \d+\n\s*\n(.*?)\n\n", text, flags=re.DOTALL)
    
    text = text[match.start():match.end()]
    lines = text.split("\n")
    lines = [l.strip() for l in lines]
    lines = [l.split("/")[0] for l in lines]
    lines.insert(0, "index")

    return lines


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

    tree = ordered_dict_rec(tree)

    return tree


def write_index(fmap, index_file):
    
    #build index
    acc = {"items": []}
    indexes = {}
    for in_file, rel_dir, out_file in fmap: 

        rel_out = rel_dir / out_file.name

        if in_file.name == "index.rst":
            index_path = tuple(rel_out.parent.parts)
            indexes[index_path] = parse_index(in_file)
        
        set_path(acc, rel_out)

    # dump index 
    items = acc.pop("items")
    acc = [v for k, v in acc.items()]
    acc.extend(items)
    acc = sort_index_tree(acc, indexes)
    acc = {"sidebar" : acc}
    
    #print(yaml.dump(acc, sort_keys=False))
    with open(index_file, "w") as fd:
        fd.write(yaml.dump(acc, sort_keys=False))

    return