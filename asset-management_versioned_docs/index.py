import yaml
import pathlib
#from collections import OrderedDict
import re

#yaml.add_representer(OrderedDict, lambda dumper, data: dumper.represent_mapping('tag:yaml.org,2002:map', data.items()))
        

# Pages that should not be included in the index / menu

skip_list = set([
    r"modules/administration/profiles/administrationtab.md",
    r"modules/administration/profiles/assistancetab.md",
    r"modules/administration/profiles/configurationtab.md",
    r"modules/administration/profiles/toolstab.md",
    r"modules/tabs/all.md",
    r"modules/tabs/changes.md",
    r"modules/tabs/contacts.md",
    r"modules/tabs/contracts.md",
    r"modules/tabs/debug.md",
    r"modules/tabs/documents.md",
    r"modules/tabs/elements.md",
    r"modules/tabs/external-links.md",
    r"modules/tabs/historical.md",
    r"modules/tabs/knowledgebase.md",
    r"modules/tabs/management.md",
    r"modules/tabs/notes.md",
    r"modules/tabs/problems.md",
    r"modules/tabs/suppliers.md",
    r"modules/tabs/templates.md",
    r"modules/tabs/tickets.md",
    r"modules/assistance/tickets/recurrentticket.md",
    r"modules/assistance/tickets/ticketadvanced.md",
    r"modules/assistance/tickets/ticketlifecycle.md",
    r"modules/assistance/tickets/ticketmanagement.md",
    r"modules/assistance/tickets/ticketopening.md",
    r"modules/configuration/plugins.md",
    r"first-steps/conclusion.md",
])


def format_menu_line(text):
    text = text.title()
    text = text.replace("_", " ")
    text = text.replace("-", " ")
    text = re.sub("GLPI", "i-Vertix ITAM", text, flags=re.IGNORECASE)
    return text


def set_path(root, path, titles):

    curr = root
    for p in path.parts:

        items = curr["items"]

        if p.endswith(".md"):

            label = format_menu_line(p[:-3])
            label = titles.get(path.as_posix(), label)
            label = format_menu_line(label)

            curr["items"].append(
                {
                    "id": p[:-3],
                    "label": label,
                }
                )
            break

        pres = [e for e in items if isinstance(e, dict) and e["id"] == p]
        if not pres:
            next_elem = {
                "id": p,
                "label": format_menu_line(p),
                "items": []
            }
            items.append(next_elem)
        else:
            next_elem = pres[0]
        
        curr = next_elem

    return root


def parse_index(fpath):
    
    text = None
    lines = []

    #print(fpath)
    with open(fpath, "r", encoding="utf8") as fd:
        text = fd.read()

    text = text + "\n\n"
    match = re.search(r"\.\. toctree::\n\s+:maxdepth: \d+\n\s*\n(.*?)\n\n", text, flags=re.DOTALL)

    if match: 
        text = text[match.start():match.end()]
        lines = text.split("\n")
        lines = [l.strip() for l in lines]
        
        #removing index from <subdir>/index
        lines = [l.split("/")[0] for l in lines]
        
        lines.insert(0, "index")

        return lines
    else:
        return []


def sort_index_tree(tree, indexes):
    
    def ordered_dict_rec(tree, indexes=indexes, cpath=[]):

        # it's a subtree, recursive call
        if isinstance(tree, dict) and "items" in tree:

            newl = list(cpath)
            newl.append(tree["id"])
                

            # Changed from OrderedDict because
            # newer python preserves key ordering
            # by default in dicts
            
            return {
                "id": tree["id"],
                "label": tree["label"],
                "items": ordered_dict_rec(
                    tree["items"], 
                    indexes,
                    newl
                    )
                }

            #return OrderedDict([
            #    ("id", tree["id"]),
            #    ("label", tree["label"]),
            #    ("items", ordered_dict_rec(
            #        tree["items"], 
            #        indexes,
            #        newl
            #        )
            #    )
            #])

        # it's a leaf 
        elif isinstance(tree, dict) and "items" not in tree:
            return tree

        # it's a list of items that should be ordered
        elif isinstance(tree, list):
            
            res = [ordered_dict_rec(x, indexes, cpath) for x in tree]

            def sorter(x): 
                index = indexes.get(tuple(cpath), [])

                if isinstance(x, dict):
                    x = x["id"]
 
                #print(f"sorter {cpath} {x} {index}")

                if x in index:
                    return index.index(x)
                
                return len(index)

            res = sorted(res, key=sorter)
            return res

        # should not happen
        elif isinstance(tree, str):
            return tree

    tree = ordered_dict_rec(tree)

    return tree


def write_index(fmap, index_file, titles):
    
    #build index
    acc = {"items": []}
    indexes = {}
    
    for c in fmap: 

        in_file = c.inf
        rel_dir = c.rel
        out_file = c.out

        rel_out = rel_dir / out_file.name

        if in_file.name == "index.rst":
            index_path = tuple(rel_out.parent.parts)
            indexes[index_path] = parse_index(in_file)

        if rel_out.as_posix() not in skip_list:
            set_path(acc, rel_out, titles)
        else:
            print(f"skipping indexing for {rel_out}")

    # dump index 
    items = acc.pop("items")
    acc = [v for k, v in acc.items()]
    acc.extend(items)
    acc = sort_index_tree(acc, indexes)
    acc = {"sidebar" : acc}

    acc["sidebar"].insert(
        1,
        {
            "id": "install",
            "label": "Installation",
            "items": [
                {
                    "id": "index",
                    "label": "Installation"
                },
                {
                    "id": "import-vm",
                    "label": "Import Virtual Machine"
                },
                {
                    "id": "configure-vm",
                    "label": "Initial Configuration",
                },
                {
                    "id": "license-vm",
                    "label": "License activation",
                },
            ]
        }                
    )
    
    #print(yaml.dump(acc, sort_keys=False))
    with open(index_file, "w") as fd:
        fd.write(yaml.dump(acc, sort_keys=False))

    return


#def replace_index(rel_dir, text, outdir):
#    
#    match = re.search(r"::: \{\.toctree .*\}\n([\w/\-\n ]*)\n:::\n", text, flags=re.MULTILINE)
#    if match is None:
#        return text
#
#    def build_link(l, rel_dir):
#
#        url = ["."]
#        
#        text = l.split("/")
#        if text[-1] == "index":
#            text.pop(-1)
#
#        if len(text) > 1 and text[-1] == text[-2]:
#            text = text[:-1]
#
#        url.extend(text)
#        url = [x for x in url if x]
#
#        link_text = text[0].title()
#        link_text= link_text.replace("_", " ")
#        link_text= link_text.replace("-", " ")
#        link_text = re.sub("GLPI", "i-Vertix ITAM", link_text, flags=re.IGNORECASE)
#
#        link_file_dest = "/".join(url) + ".md"
#        if (outdir / rel_dir / link_file_dest).exists():
#            #pointing to a file
#            url = link_file_dest
#        else:
#            # pointing to a directory
#            if url[-1] != "":
#                # docusaurus needs a / at the end of the link...
#                url.append("")
#                url = "/".join(url)
#
#        #print(f"BL {rel_dir} {url} {test}")
#
#        return (link_text, url)
#                                        
#    links = match.group(1).split()
#    links = [build_link(l, rel_dir) for l in links]
#    links = [f"- [{text}]({url})" for text, url in links]
#    links = "\n".join(links)
#
#    text = text[:match.start()] + links + "\n" + text[match.end():]
#    
#    return text


def replace_index(rel_dir, text, outdir):
    
    match = re.search(r"::: \{\.toctree .*\}\n([\w/\-\n ]*)\n:::\n", text, flags=re.MULTILINE)
    if match is None:
        return text
    
    links = "<DocCardList />"
    text = text[:match.start()] + links + "\n" + text[match.end():]

    text = text.split("\n")
    text.insert(4, "import DocCardList from '@theme/DocCardList';")
    text = "\n".join(text) 
    
    return text


def parse_titles(fmap):

    res = {}

    for c in fmap: 

        rel_file = (c.rel / c.out.name).as_posix()
        
        with open(c.inf, "r", encoding="utf-8") as fd:
            text = fd.readlines()
            if text[1][0] in ["=", "~", "-"]:
                res[rel_file] = text[0].strip()
            else:
                res[rel_file] = c.inf.with_suffix("").name


    for r in res:
        print(f"{r} -> {res[r]}")

    return res