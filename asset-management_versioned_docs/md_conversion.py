import os
import pathlib
import json
import subprocess as sb
import argparse
import shutil
import re

import index 
import images
import utils


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

            
def convert_to_md(in_path, out_path):
    #print(f"converting {in_path} {out_path}")
    utils.makedir(out_path)
    sb.call(["pandoc", in_path, "-f",  "rst", "-t", "commonmark_x", "-o", out_path])
    return


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

    def remove_ref(text):

        end = 0
        while True:
            match = re.search(r":ref:`(.*?) <(.*?)>`", text[end:], flags=re.MULTILINE)
            if not match:
                break

            new_text = f"{match.group(1)}"
            text = text[:end + match.start()] + new_text + text[end + match.end():]

            end += match.start() + len(new_text)

        return text

    transforms = [
        lambda x: x.replace(".. figure::", ".. image::"),
        lambda x: x.replace(".. include:: /modules/tabs", ".. include:: ../tabs"),
        lambda x: x.replace(":orphan:\n", ""),
        lambda x: x.replace("authentification", "authentication"),
        remove_ref
    ]
 
    for f in files:

        text = ""
        with open(f, "r", encoding="utf8") as fd:
            text = fd.read()

        for t in transforms:
            
            if isinstance(t, tuple):
                check, t = t
                if check(f, text):
                    text = t(text)
            
            elif(callable(t)):
                text = t(text)
            
            else:
                print("Error applying the transform!")
                print("please provide a (check(), transform()) tuple or a transform()")

        with open(f, "w", encoding="utf8") as fd:
            fd.write(text)

    return


def parse_link(conv_list):

    links = {}
    
    # orig_link -> correction, to manage rst includes
    # without parsing the full include tree
    links_euristic = {}
    
    links_nr = 0

    for inf, rel, outf in conv_list:
        with open(inf, "r", encoding="utf8") as fd:
            text = fd.read()

        end = 0
        while True:
            match = re.search(r":doc:`(.*?) <(.*?)>`", text[end:], flags=re.MULTILINE)
            if not match:
                break

            links_nr += 1

            #l_text = match.group(1)
            l_path = match.group(2)

            if l_path[0] == "/":
                norm_path = l_path.split("/")
                norm_path = [n for n in norm_path if n]
            else:
                norm_path = utils.merge_path(rel.parts, l_path.split("/"))

            if norm_path[-1] == "index":
                norm_path = norm_path[:-1]

            if norm_path[-1] == norm_path[-2]:
                norm_path = norm_path[:-1]


            #print("")
            #print(inf, l_text)
            #print(rel.parts, l_path)
            #print(norm_path)
            ##print(l_text, l_path)

            norm_path = ["", "asset-management"] + norm_path
            url = "/".join(norm_path)
            links[(outf, l_path)] = url
            links_euristic[l_path] = url

            end += match.end()

    print(f"internal links: {links_nr}")
    return links, links_euristic


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

    # parse links
    link_replacement, links_euristic = parse_link(fmap)

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

    #images
    assets_dir = output_dir / "assets"
    assets_dir.mkdir(exist_ok=True)
    incpath_to_realpath = images.process_images(
        fmap, 
        input_dir,
        assets_dir,
        real_copy=args.copy_images 
        )


    if args.skip_post:
        exit(0)
        
    tot_links = 0
    replaced_links = 0

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
        
        # convert indexes 
        text = index.replace_index(rel_dir, text) 

        # replace glpi_address
        text = text.replace("{glpi_address}", "glpi_address")
        
        # Removing all { .attrib=value }
        text = re.sub(r"\{.*?\}", "", text, flags=re.DOTALL)

        # Convert links


        while True:
            match = re.search(r"\`([\-\w \"\'>]+) <([ \.\w/_\-]+)>\`", text, flags=re.MULTILINE)
            if not match:
                break

            link_text = match.group(1)
            link_path = match.group(2)

            k = (f, link_path)
            url = link_replacement.get(k)
            tot_links += 1

            if url is None:
                replaced_links += 1
                url = links_euristic.get(link_path, link_path)

            #url = url.replace(" ", "")

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
        lambda x: re.sub(r"^-[ ]+[\n]+\s*", r"- ", x, flags=re.MULTILINE),
    ]

    
    for inf, rel_dir, f in fmap:
    
        lines = []
        with open(f, "r", encoding="utf8") as fd:
            text = fd.read()

        for r in transforms:
            text = r(text)
        
        with open(f, "w", encoding="utf8") as fd:
            fd.write(text)
        
    print(f"tot_links: {tot_links}")
    print(f"replaced_links: {replaced_links}")

