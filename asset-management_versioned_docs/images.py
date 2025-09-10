import pathlib
import re
import shutil
import utils

def process_images(
        fmap, 
        input_dir,
        assets_dir,
        real_copy=False):

    # parse / copy all images
    images = []
    img_include_from = {}
    
    incpath_to_realpath = {}
    realpath_to_incpath = {}

    img_nr = 0
    for c in fmap:

        lines = []
        with open(c.out, "r", encoding="utf8") as fd:
            lines = fd.readlines()

        for l in lines:
            img_include = re.search(r"!\[(.*)\]\((.*)\)", l)

            if img_include:
                img_nr += 1
                orig_img = img_include.group(2)
                img = pathlib.Path(orig_img)
                
                #if it is relative, make it absolute
                #if not img.is_absolute():
                img = utils.merge_path(c.rel.parts, img.parts)
                img = pathlib.Path(*img)
                if img.parts[0] == "\\":
                    img = pathlib.Path(*img.parts[1:])

                images.append(img)
                incpath_to_realpath[orig_img] = img
                
                # I need a bi-directional association for replacements
                realpath_to_incpath[img] = orig_img

                img_include_from[img] = c.out

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
 
        if real_copy:
            if in_path.exists():
                out_path = assets_dir / c
                utils.makedir(out_path)
                print(f"{in_path} -> {out_path}")
                shutil.copy(in_path, out_path)
            else:
                print(f"image {in_path} does not exist")

    return incpath_to_realpath


## replacing image paths to point to the 
## asset dir
def replace_image(match, rel_dir, incpath_to_realpath):
    path = match.group(2)
    link = incpath_to_realpath[path] 

    lev = len(rel_dir.parts) * [".."]
    lev = pathlib.Path(*lev)
    link = lev / "assets" / link
    link = link.as_posix()
    new_text = f"![{match.group(1)}]({link})"
    
    return new_text
