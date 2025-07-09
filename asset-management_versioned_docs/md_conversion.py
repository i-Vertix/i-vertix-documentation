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


def normalize_url(url):
    comp = url.split("/")
    if comp:
            
        if comp[-1] == "index":
            comp = comp[:-1]
            if comp[0] == "..":
                comp = comp[1:]

        #url starts with an "/", hence it is absolute
        if comp[0] == "":
 
            if comp[0] not in ["/asset-management", ".."]:
                comp.insert(0, "/asset-management")

    comp = filter(lambda x: len(x) > 0, comp)
    return "/".join(comp)


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
                "label": p.title().replace("_", " "),
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


def makedir(path):
    dpath = os.path.dirname(path)
    if not os.path.exists(dpath):
        os.makedirs(dpath, exist_ok=True)
    return


def convert_to_md(in_path, out_path):
    #print(f"converting {in_path} {out_path}")
    
    makedir(out_path)
    
    #sb.call(["pandoc", in_path, "-f",  "rst", "-t", "markdown_strict", "-o", out_path])
    #sb.call(["pandoc", in_path, "-f",  "rst", "-t", "markdown", "-o", out_path])
    sb.call(["pandoc", in_path, "-f",  "rst", "-t", "commonmark_x", "-o", out_path])
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


def merge_path(base, rel):  
    
    if rel.startswith("/"):
        return rel                  
    
    base_parts = list(pathlib.Path(base).parts)
    rel_parts = list(pathlib.Path(rel).parts)
    #print(base_parts, rel_parts)
    while rel_parts[0] == "..":
        base_parts = base_parts[:-1]
        rel_parts = rel_parts[1:]

    merged_parts = base_parts + rel_parts   
    #print(merged_parts)
    return "/".join(merged_parts)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="GLPI doc converter",
        description='What the program does',
        epilog='Text at the bottom of help'
        )

    parser.add_argument("input_dir")
    parser.add_argument("output_dir")
    parser.add_argument("--skip_conversion", action="store_true", default=False)
    parser.add_argument("--skip_post", action="store_true", default=False)

    args = parser.parse_args()

    input_dir = args.input_dir
    output_dir = args.output_dir

    if input_dir[-1] != "/":
        input_dir = f"{input_dir}/"
    
    if output_dir[-1] != "/":
        output_dir = f"{output_dir}/"

    os.makedirs(output_dir, exist_ok=True)

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
            if not args.skip_conversion:
                convert_to_md(in_path, out_path)
                add_header(out_path)
            set_path(acc, pathlib.Path(rel_path))

    items = acc.pop("items")
    acc = [v for k, v in acc.items()]
    acc.extend(items)
    acc = sort_index_tree(acc, indexes)
    acc = {"sidebar" : acc}
    
    #print(yaml.dump(acc, sort_keys=False))
    with open("asset-management_versioned_sidebars/10-sidebar.yaml", "w") as fd:
        fd.write(yaml.dump(acc, sort_keys=False))

    
    # parse / copy all common images
    static_dir = os.path.join(output_dir, "assets")
    os.makedirs(static_dir, exist_ok=True)
    common_images = []
    path_translation = {}

    img_nr = 0
    for f in out_files:

        lines = []
        with open(f, "r", encoding="utf8") as fd:
            lines = fd.readlines()

        for l in lines:
            img_include = re.search(r"!\[(.*)\]\((.*)\)", l)

            if img_include:
                img_nr += 1
                img = img_include.group(2)
                orig_img = img
                
                #if it is relative, make it absolute
                if img[0] != "/":
                    rel_out_path = f.replace(output_dir, "")
                    img = "/" + merge_path(os.path.dirname(rel_out_path), img)
                
                common_images.append(img)
                path_translation[orig_img] = img

    print(f"images nr: {img_nr}")
    common_images = list(set(common_images))
    print(f"images dedup: {len(common_images)}")

    replaced_links = {}
    for c in common_images:
        
        in_path = os.path.join(input_dir, c[1:])
        if not os.path.exists(in_path): 
            print(f"Image {in_path} does not exist")

            fname = os.path.basename(c)
            replacements = list(filter(lambda x: x.find(fname) != -1 and x != c, common_images))

            if replacements:
                in_path = os.path.join(input_dir, replacements[0][1:])
                print(f"replacing with: {in_path}")
            else:
                print("Cannot replace")
                continue
            
            if not os.path.exists(in_path): 
                print(f"Replacement {in_path} still does not exist")
                continue

            replaced_links[c] = replacements[0]
 
        out_path = os.path.join(static_dir, c[1:])
        makedir(out_path)

        shutil.copy(in_path, out_path)
        #print("common", c)
        #print("dest", out_path)


    if args.skip_post:
        exit(0)

    for f in out_files:

        text = ""
        with open(f, "r", encoding="utf8") as fd:
            text = fd.read()
        
        # removing todo
        while True:
            match = re.search(r"::: {\.todo}\n(.*?):::\n", text, re.DOTALL)
            
            if match is None:
                break
            
            text = text[:match.start()] + text[match.end():]
        
        
        # Removing all { .attrib=value }

        text = text.replace("{glpi_address}", "glpi_address")
        text = re.sub(r"\{.*?\}", "", text, flags=re.DOTALL)


        # Convert links
        while True:
            match = re.search(r"\`([\-\w \"\'>]+) <([ \.\w/_\-]+)>\`", text, flags=re.MULTILINE)
            if not match:
                break

            link_text = match.group(1)
            url = normalize_url(match.group(2))

            url = url.replace(" ", "")
            new_text = f"[{link_text}]({url})"
            text = text[:match.start()] + new_text + text[match.end():]


        #boxes conversion
        while True:
            match = re.search(r"> \[\!(\w+)\]((\n>.*)+)", text, flags=re.MULTILINE)
            
            if match is None:
                break
                
            note_type = match.group(1).lower()
            if note_type == "note":
                note_type = "info"

            note_text = match.group(2)
            note_text = re.sub(r"^> *", "", note_text, flags=re.MULTILINE)
            note_text = note_text.strip()
            
            new_text = f":::{note_type}\n\n{note_text}\n\n:::"
            new_text = new_text.replace(" <", " \\<")

            text = text[:match.start()] + new_text + text[match.end():]

        # more boxes conversion, some boxes are still present... 
        while True:
            match = re.search(r"\s*::::\s*\n\s*:::\s*\n\s*(.*?)\s*:::\n(.*?)\s*::::", text, re.DOTALL)
            
            if match is None:
                break

            note_type = match.group(1).lower().strip()
            if note_type == "hint":
                note_type = "tip"
                
            note_text = match.group(2).replace("> ", "")
            new_text = f"\n:::{note_type}\n{note_text}\n:::"
            text = text[:match.start()] + new_text + text[match.end():]

        # even more boxes, this time with custom title
        end = 0
        while True:
            match = re.search(r"\s*:::\s*\n((?:\*\*)Ex[a|e]mple.*?)\n\s*(.*?)\s*:::\n", text[end:], re.DOTALL)
            
            if match is None:
                break
            
            new_text = f"\n:::note[{match.group(1)}]\n\n{match.group(2)}\n:::\n"
            text = text[:end+match.start()] + new_text + text[end+match.end():]
            end += match.start() + len(new_text)

        while True:
            match = re.search(r"\[([^\]]*\n[^\]]*)\]\((.*)\)", text, flags=re.MULTILINE)
            if match is None:
                break
            
            #Removing newlines in link text
            link_text = match.group(1).replace("\n", " ")
            new_text = f"[{link_text}]({match.group(2)})"
            text = text[:match.start()] + new_text + text[match.end():]
        
        # Changing GLPI to i-Vertix ITAM
        text = text.replace("GLPI", "i-Vertix ITAM")
        
        #convert indexes
        if os.path.basename(f) == "index.md":
            
            match = re.search(r"::: \n([\w/\-\n ]*)\n:::\n", text, flags=re.MULTILINE)            
 
            if match:
            
                rel_dir = f.replace(output_dir, "")
                rel_dir = list(pathlib.Path(rel_dir).parts)
                if rel_dir[-1] == "index.md":
                    rel_dir.pop(-1)

                def build_link(l, rel_dir):
                    url = ["/asset-management"]
                    url.extend(rel_dir)
                    
                    text = l.split("/")
                    if text[-1] == "index":
                        text.pop(-1)

                    url.extend(text)
                    url = [x for x in url if x]

                    link_text = text[0].title()
                    link_text= link_text.replace("_", " ")
                    link_text= link_text.replace("-", " ")

                    return (link_text, "/".join(url))
                                                    
                links = match.group(1).split()
                links = [build_link(l, rel_dir) for l in links]
                links = [f"- [{text}]({url})" for text, url in links]
                links = "\n".join(links)

                text = text[:match.start()] + links + "\n" + text[match.end():]
        

        while True:
            match = re.search(r"<((?:https*|redis+)://.*)>", text)
            if not match:
                break
            
            url = match.group(1)
            new_text = f"[{url}]({url})"
            text = text[:match.start()] + new_text + text[match.end():]

        
        match = re.search(r"<(.*@.*) .*>", text)
        if match:
            url = match.group(1)
            new_text = url
            text = text[:match.start()] + new_text + text[match.end():]
        
        # replacing image paths to point to the 
        # asset dir
        end = 0
        while True:
            match = re.search(r"!\[(.*)\]\((.*)\)", text[end:])
            if not match:
                break

            path = match.group(2)
            link = path_translation[path] 

            lev = len(pathlib.Path(f).parts)-3
            lev = "/".join(lev * [".."] + ["assets"])
            link = lev + link

            new_text = f"![{match.group(1)}]({link})"
            text = text[:end + match.start()] + new_text + text[end + match.end():]
            end += match.start() + len(new_text)

        if os.path.basename(f) == "cli.md":
            text = ""
        
        with open(f, "w", encoding="utf8") as fd:
            fd.write(text)
     
    transforms = [
        lambda x: x.replace("\\\'", "'"),
        lambda x: x.replace("\\\"", "\""),
        lambda x: x.replace("\\.", "."),
        lambda x: re.sub(r"style=\".*\"", "", x),
        lambda x: re.sub(r"^export", r"\\export", x, flags=re.MULTILINE),
    ]

    
    for f in out_files:
    
        lines = []
        with open(f, "r", encoding="utf8") as fd:
            text = fd.read()

        for r in transforms:
            text = r(text)
        
        with open(f, "w", encoding="utf8") as fd:
            fd.write(text)
