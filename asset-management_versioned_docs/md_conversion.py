import os
import pathlib
import json
import subprocess as sb
import argparse
import shutil
import re

import index 


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

            module_name = os.path.basename(file_path)
            module_name = module_name[:-3]
            title = module_name.title()
            title = title.replace("-", " ")

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
    return

            


def makedir(path):
    path.parent.mkdir(exist_ok=True, parents=True)
    return


def convert_to_md(in_path, out_path):
    #print(f"converting {in_path} {out_path}")
    makedir(out_path)
    sb.call(["pandoc", in_path, "-f",  "rst", "-t", "commonmark_x", "-o", out_path])
    return


def merge_path(base, rel):  

    base_parts = list(base.parts)
    rel_parts = list(rel.parts)    
    while rel_parts[0] == "..":
        base_parts = base_parts[:-1]
        rel_parts = rel_parts[1:]

    merged_parts = base_parts + rel_parts   
    
    return pathlib.Path(*merged_parts)


def compute_conversion_list(input_dir, output_dir):
    """
    returns a list of (input_file, relative path in input dir, output_file)
    """
    
    res = []
    for root, _, files in input_dir.walk():
            
        rst_files = filter(lambda x: x.endswith(".rst"), files)
        for f in rst_files:
            
            in_path = root / f

            rel_path = in_path.relative_to(input_dir)
            rel_dir = rel_path.parent
            
            out_path = output_dir / rel_path.with_suffix(".md")

            res.append((in_path, rel_dir, out_path))
    
    return res



# The alternative is keeping a fork of the GLPI doc repository
def prepare_sources(files):
    """

    """

    transforms = [
        (
            lambda path, text: True, 
            lambda x: x.replace(".. figure::", ".. image::")
        ),

        (
            lambda path, text: True, 
            lambda x: x.replace(".. include:: /modules/tabs", ".. include:: ../tabs")
        )

    ]
 
    for f in files:

        text = ""
        with open(f, "r", encoding="utf8") as fd:
            text = fd.read()

        for check, t in transforms:
            if check(f, text):
                text = t(text)

        with open(f, "w", encoding="utf8") as fd:
            fd.write(text)

    return
    

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="GLPI doc converter",
        description='What the program does',
        epilog='Text at the bottom of help'
        )

    parser.add_argument("input_dir")
    parser.add_argument("output_dir")
    parser.add_argument("--skip-conversion", action="store_true", default=False)
    parser.add_argument("--skip-post", action="store_true", default=False)
    parser.add_argument("--copy-images", action="store_true", default=False)
    parser.add_argument("--tmp-dir", default="itam_tmp", dest="tmp_dir")
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
    fmap = compute_conversion_list(input_dir, output_dir)
   
    # fix errors in glpi sources, 
    # fix hard (for pandoc) to interpret rst directives
    prepare_sources([x[0] for x in fmap])

    # create md files as result from pandoc conversion    
    if not args.skip_conversion:
        for in_file, rel_dir, out_file in fmap: 
            convert_to_md(in_file, out_file)
    
    # write docusaurs header to files
    for _, _, out_file in fmap: 
        add_header(out_file)

    # compute and write the index yaml file
    index.write_index(
        fmap, 
        "asset-management_versioned_sidebars/10-sidebar.yaml"
    )

    # parse / copy all images
    static_dir = output_dir / "assets"
    static_dir.mkdir(exist_ok=True)
    images = []
    img_include_from = {}
    
    incpath_to_realpath = {}
    realpath_to_incpath = {}

    img_nr = 0
    for _, rel_path, f in fmap:

        lines = []
        with open(f, "r", encoding="utf8") as fd:
            lines = fd.readlines()

        for l in lines:
            img_include = re.search(r"!\[(.*)\]\((.*)\)", l)

            if img_include:
                img_nr += 1
                orig_img = img_include.group(2)
                img = pathlib.Path(orig_img)
                
                #if it is relative, make it absolute
                #if not img.is_absolute():
                img = merge_path(rel_path, img)
                if img.parts[0] == "\\":
                    img = pathlib.Path(*img.parts[1:])

                images.append(img)
                incpath_to_realpath[orig_img] = img
                
                # I need a bi-directional association for replacements
                realpath_to_incpath[img] = orig_img

                img_include_from[img] = f

    print(f"images nr: {img_nr}")
    images = list(set(images))
    print(f"images dedup: {len(images)}")

    replacements = {x.name: x  for x in images if (input_dir / x).exists()}

    for c in images:

        in_path = input_dir / c

        # if image does not exist, search for an image with the same name
        # if a replacement is found, then replace just the entry 
        # in incpath_to_realpath, avoiding multiple copies of the same
        # image

        if not in_path.exists(): 
            print(f"Image {in_path}, included from {img_include_from[c]} does not exist")

            if c.name in replacements:
                incpath = realpath_to_incpath[c]
                incpath_to_realpath[incpath] = replacements[c.name]
                print(f"-> Replaced with {replacements[c.name]}")
                continue
 
        if args.copy_images:
            out_path = static_dir / c
            makedir(out_path)
            shutil.copy(in_path, out_path)


    if args.skip_post:
        exit(0)

    # files processing
    for _, rel_dir, f in fmap:

        text = ""
        with open(f, "r", encoding="utf8") as fd:
            text = fd.read()
        
        # removing todo
        while True:
            match = re.search(r"::: {\.todo}\n(.*?):::\n", text, re.DOTALL)
            
            if match is None:
                break
            
            text = text[:match.start()] + text[match.end():]
        
        

        text = text.replace("{glpi_address}", "glpi_address")
        
        # Removing all { .attrib=value }
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
            match = re.search(r"^[> ]*\[\!(\w+)\]((\n>.*)+)", text, flags=re.MULTILINE)
            
            if match is None:
                break
                
            note_type = match.group(1).lower()
            if note_type == "note":
                note_type = "info"

            note_text = match.group(2)
            note_text = re.sub(r"^>[ >]*", "", note_text, flags=re.MULTILINE)
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
        if f.name == "index.md":
            
            match = re.search(r"::: \n([\w/\-\n ]*)\n:::\n", text, flags=re.MULTILINE)            
 
            if match:

                def build_link(l, rel_dir):
                    url = ["/asset-management"]
                    url.extend(list(rel_dir.parts))
                    
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

        
        #replace e-mail addresses
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
            link = incpath_to_realpath[path] 

            lev = len(rel_dir.parts) * [".."]
            lev = pathlib.Path(*lev)
            link = lev / "assets" / link
            link = link.as_posix()
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

    
    for inf, rel_dir, f in fmap:
    
        lines = []
        with open(f, "r", encoding="utf8") as fd:
            text = fd.read()

        for r in transforms:
            text = r(text)
        
        with open(f, "w", encoding="utf8") as fd:
            fd.write(text)
