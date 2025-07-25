import json


def makedir(path):
    path.parent.mkdir(exist_ok=True, parents=True)
    return


def merge_path(base, rel):  

    base_parts = list(base)
    rel_parts = list(rel)
    while rel_parts[0] == "..":
        base_parts = base_parts[:-1]
        rel_parts = rel_parts[1:]

    merged_parts = base_parts + rel_parts   
    
    return merged_parts


def dump_struct(s):
    print(json.dumps(s, indent=4))
    return


#def normalize_url(url):
#    comp = url.split("/")
#    if comp:
#            
#        if comp[-1] == "index":
#            comp = comp[:-1]
#            if comp[0] == "..":
#                comp = comp[1:]
#
#        #url starts with an "/", hence it is absolute
#        if comp[0] == "":
# 
#            if comp[0] not in ["/asset-management", ".."]:
#                comp.insert(0, "/asset-management")
#
#    comp = filter(lambda x: len(x) > 0, comp)
#    return "/".join(comp)