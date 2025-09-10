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


ConvSpec = namedtuple("ConvSpec", "inf, rel, out, orig_out")


#def add_header(file_path, titles, out_dir):
def add_header(file_path):

    lines = []
    with open(file_path, "r", encoding="utf8") as fd:
        lines = fd.readlines()
            
    if lines:
        if not (lines[0].startswith('---') or lines[0].startswith(r'\-\--')):

            module_name = file_path.with_suffix("").name
            title = index.format_menu_line(module_name)

            #title_key = file_path.relative_to(out_dir).as_posix()
            #title = titles.get(title_key, module_name.title())

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


def compute_conversion_list(input_dir, output_dir, skip_list=[]):
    """
    returns a list of (input_file, relative path in input dir, output_file)
    """
    
    res = []
    for root, _, files in input_dir.walk():
            
        rst_files = filter(lambda x: x.endswith(".rst"), files)
        for f in rst_files:
            
            in_path = root / f

            rel_path = in_path.relative_to(input_dir)

            if rel_path.as_posix() in skip_list:
                print(f"skipping {rel_path}")
                continue

            rel_dir = rel_path.parent
            
            out_filename = rel_path.name
            out_filename = out_filename.replace("glpi", "itam")
            
            orig_out = output_dir / rel_path.with_suffix(".md")
            
            rel_path = rel_path.with_name(out_filename)
            out_path = output_dir / rel_path.with_suffix(".md")

            res.append(ConvSpec(in_path, rel_dir, out_path, orig_out))
    
    return res
    
    
def overwrite_files(overwrite_dir, output_dir):

    print(overwrite_dir)

    for root, _, files in overwrite_dir.walk():

        for f in files: 
            ov_path = root / f
            ov_rel_path = ov_path.relative_to(overwrite_dir)
            src = overwrite_dir / ov_rel_path
            dst = output_dir / ov_rel_path
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(src, dst)

            print(f"overwriting: {src} -> {dst}")

    return



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


def provide_link_corrections(url):

    alt = [
        url.parent / url.stem / pathlib.Path("index.md"),
        url.parent / url.name.replace(".html", ""),
        url.parent / url.name.split(".")[0] / (url.name.split(".")[0] + ".md"),
    ]

    return alt


def test_url(outf, url):

    rel_path = pathlib.Path(url)
    fs_path = outf.parent / rel_path.with_suffix(".md")
    return fs_path.exists()


#Looks for url with a given list of replacements
def correct_url(outf, url):

    rel_path = pathlib.Path(url)
    for a in provide_link_corrections(rel_path):
        abs_path = outf.parent / a
        if abs_path.exists():
            return a.as_posix()
    
    return None


def parse_link(conv_list):

    links = {}
    
    # orig_link -> correction, to manage rst includes
    # without parsing the full include tree
    links_euristic = {}

    # second euristic,
    # for broken links in orig sources
    # last part of the link -> working link with the same last part
    links_dest = {}

    dead_url = []
    
    links_nr = 0

    for c in conv_list:

        inf = c.inf
        rel = c.rel
        outf = c.out

        with open(inf, "r", encoding="utf8") as fd:
            text = fd.read()

        for match in re.finditer(r"(?::doc:)*`(.*?) <(.*?)>`", text, flags=re.MULTILINE):

            links_nr += 1

            #l_text = match.group(1)
            l_path = match.group(2)
            if l_path.startswith("http"):
                continue
            #    links[(outf, l_path)] = l_path
            #    continue

            if l_path[0] == "/":
                norm_path = l_path.split("/")
                norm_path = [n for n in norm_path if n]
            else:
                norm_path = utils.merge_path(rel.parts, l_path.split("/"))

            if norm_path[-1] == "index":
                norm_path = norm_path[:-1]

            if len(norm_path) > 1 and norm_path[-1] == norm_path[-2]:
                norm_path = norm_path[:-1]

            #norm_path = ["", "asset-management"] + norm_path
            url = "/".join([".."] * len(rel.parts) + norm_path)

            if not test_url(outf, url):
                replaced_url = correct_url(outf, url)
                if replaced_url is None:
                    dead_url.append((outf, l_path, rel, norm_path))
                    continue
                else:
                    url = replaced_url
                    links_dest[replaced_url.split("/")[-1]] = replaced_url
            else:
                links_dest[url.split("/")[-1]] = norm_path

                # test is performed with .md suffix, if success add the md extension
                # to point to the files, instead of http paths/endpoints
                url = f"{url}.md"

            # we can store the final url
            #links[(outf, l_path)] = url
            #print(url)
            links[(outf, l_path)] = url

            # we need to store the relative path of the url,
            # it will be joined with a number of ".." depending 
            # the link starting point
            links_euristic[l_path] = norm_path
    
    for outf, l_path, rel, norm_path in dead_url:
        name = norm_path[-1]
        if name in links_dest:
            norm_path = links_dest[name]
            url = "/".join([".."] * len(rel.parts) + norm_path)
            links[(outf, l_path)] = url
            print(f"Replacing {name} in {outf} with {url}")
            

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
    parser.add_argument(
        "--overwrite-dir", 
        default="asset-management_versioned_docs/itam_overwrite", 
        dest="overwrite_dir"
        )
    
    parser.add_argument(
        "--overwrite-only", 
        action="store_true", 
        default=False, 
        dest="overwrite_only"
        )
    
    args = parser.parse_args()

    input_dir = pathlib.Path(args.input_dir)
    output_dir = pathlib.Path(args.output_dir)
    tmp_dir = pathlib.Path(args.tmp_dir)
    overwrite_dir = pathlib.Path(args.overwrite_dir)

    output_dir.mkdir(exist_ok=True)

    if args.overwrite_only:
        overwrite_files(overwrite_dir, output_dir)
        exit(0)

    
    # copy tmp dir    
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)

    shutil.copytree(input_dir, tmp_dir)
    input_dir = tmp_dir

    # compute the list of (input, red_dir, output) that will be used in all
    # following ops
    fmap = compute_conversion_list(
        input_dir, 
        output_dir,
        skip_list=[
            r"modules/configuration/general/glpi_network.rst",
            r"first-steps/conclusion.rst",
            r"modules/configuration/plugins.rst",
            r"cli.rst",
            ]
        )
   
    # fix errors in glpi sources, 
    # fix hard (for pandoc) to interpret rst directives
    prepare_sources([x[0] for x in fmap])

    page_titles = index.parse_titles(fmap)

    # create md files as result from pandoc conversion    
    if not args.skip_conversion:
        for c in fmap: 
            convert_to_md(c.inf, c.out)
    
    # parse links
    link_replacement, links_euristic = parse_link(fmap)
    titles = index.parse_titles(fmap)
    
    # write docusaurs header to files
    for c in fmap: 
        #add_header(c.out, titles, output_dir)
        add_header(c.out)

    # compute and write the index yaml file
    index.write_index(
        fmap, 
        "asset-management_versioned_sidebars/10-sidebar.yaml",
        titles
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

    def replace_links(match, rel_dir, outfile):

        global tot_links
        global replaced_links

        link_text = match.group(1)
        link_path = match.group(2)

        k = (outfile, link_path)
        url = link_replacement.get(k)
        tot_links += 1

        if url is None:
            replaced_links += 1
            url = links_euristic.get(link_path)
            if url is None:
                return link_text
            
            url = "/".join([".."] * len(rel_dir.parts) + url)

        new_text = f"[{link_text}]({url})"
        return new_text


    def replace_boxes(match):
        note_type = match.group(1).lower()
        if note_type == "note":
            note_type = "info"

        note_text = match.group(2)
        note_text = re.sub(r"^[ >]*", "", note_text, flags=re.MULTILINE)
        note_text = note_text.strip()
        
        new_text = f":::{note_type}\n\n{note_text}\n\n:::"
        new_text = new_text.replace(" <", " \\<")
        return new_text


    def replace_boxes2(match):

        note_type = match.group(1).lower().strip()
        if note_type == "hint":
            note_type = "tip"
            
        note_text = match.group(2).replace("> ", "")
        return f"\n:::{note_type}\n{note_text}\n:::"


    def replace_boxes_custom_title(match):
        new_text = f"\n:::note[{match.group(1)}]\n\n{match.group(2)}\n:::\n"
        return new_text
        

    def remove_newlines_in_link_text(match):
        link_text = match.group(1).replace("\n", " ")
        new_text = f"[{link_text}]({match.group(2)})"
        return new_text


    transforms = [

        # using re.sub passing a function that returns the replacement
        
        # remove todo
        lambda x, _, f: re.sub(r"::: {\.todo}\n(.*?):::\n", "", x, flags=re.DOTALL),

        # replace index
        lambda x, rd, f: index.replace_index(rd, x, output_dir),

        # replace glpi_address
        lambda x, _, f: x.replace("{glpi_address}", "itam_address"),
        lambda x, _, f: x.replace("glpi://", "itam://"),
        lambda x, _, f: x.replace("glpi-project", "itam-project"),
        
        # Removing all { .attrib=value }
        lambda x, _, f: re.sub(r"\{.*?\}", "", x, flags=re.DOTALL),

        lambda x, rd, f: re.sub(
            r"\`([\-\w \"\'>]+) <([ \.\w/_\-]+)>\`", 
            partial(replace_links, rel_dir=rd, outfile=f), 
            x, 
            flags=re.MULTILINE),
        
        lambda x, _, f: re.sub(r"^[> ]*\[\!(\w+)\]((\n[> ]+.*)+)", 
                            replace_boxes,
                            x, 
                            flags=re.MULTILINE),

        lambda x, _, f: re.sub(r"\s*::::\s*\n\s*:::\s*\n\s*(.*?)\s*:::\n(.*?)\s*::::", 
                            replace_boxes2, 
                            x, 
                            flags=re.DOTALL),

        lambda x, _, f: re.sub(r"\s*:::\s*\n((?:\*\*)Ex[a|e]mple.*?)\n\s*(.*?)\s*:::\n", 
                            replace_boxes_custom_title, 
                            x, 
                            flags=re.DOTALL),

        lambda x, _, f: re.sub(r"\[([^\]]*\n[^\]]*)\]\((.*)\)", remove_newlines_in_link_text, x, flags=re.MULTILINE),

        # Changing GLPI to i-Vertix ITAM
        lambda x, _, f: x.replace("GLPI", "i-Vertix ITAM"),
        
        # replace https and redis links, for some reason they are converted wrongly
        lambda x, _, f: re.sub(r"<((?:https*|redis+)://.*)>", lambda m: f"[{m.group(1)}]({m.group(1)})", x),

        # convert email addresses
        lambda x, _, f: re.sub(r"<(.*@.*) .*>", lambda m: m.group(1), x),

        # replace all image path with relative links in the asset directory,
        # using a partial functions to fix arguments in images.replace_image
        lambda x, rd, f: re.sub(
            r"!\[(.*)\]\((.*)\)", 
            partial(
                images.replace_image, 
                rel_dir=rd, 
                incpath_to_realpath=incpath_to_realpath), 
            x),

        # adds escape chars
        lambda x, _, f: x.replace("\\\'", "'"),
        lambda x, _, f: x.replace("\\\"", "\""),
        lambda x, _, f: x.replace("\\.", "."),
        
        # removes style= tags
        lambda x, _, f: re.sub(r"style=\".*\"", "", x),

        # escapes "export" at the beginning of lines that are interpreted as
        # react syntax
        lambda x, _, f: re.sub(r"^export", r" export", x, flags=re.MULTILINE),
        
        lambda x, _, f: re.sub(r"^-[ ]+[\n]+\s*", r"- ", x, flags=re.MULTILINE),
        
        # handles semicolons at the beginning of the line with some spaces after
        lambda x, _, f: re.sub(r"^:\s[\s]+", r"    ", x, flags=re.MULTILINE),

        # Replace (spaces):(spaces) with the same number of spaces to 
        # keep indent level
        lambda x, _, f: re.sub(
            r"^\s*:\s[\s]+", 
            lambda x: " " * (x.end()-x.start() - 1), 
            x, flags=re.MULTILINE),

        # replaces some links with just the text        
        lambda x, _, f: re.sub(r"\[([\w \\>\n:\./!\+]*)\](?!\()", r"*\1*", x, flags=re.MULTILINE),
    
    ]
    
    #for inf, rel_dir, f in fmap:
    for c in fmap:

        inf = c.inf
        rel_dir = c.rel
        f = c.out
        
        lines = []
        with open(f, "r", encoding="utf8") as fd:
            text = fd.read()
        
        if f.name == "cli.md":
            text = ""

        for r in transforms:
            text = r(text, rel_dir, f)
        
        with open(f, "w", encoding="utf8") as fd:
            fd.write(text)
        
    print(f"tot_links: {tot_links}")
    print(f"replaced_links: {replaced_links}")


    # Then, overwriting some of the md files, needed for some rst
    # files for which search/replace is not enough
    overwrite_files(overwrite_dir, output_dir)

