import sys
import re



if __name__ == "__main__":

    f = sys.argv[1]

    text = ""
    with open(f, "r", encoding="utf8") as fd:
        text = fd.read()

    #match = re.search(r":::: ([\w]+)\s*::: title\s*(.*?)\s*:::\s*(.*?)::::\s*", text, re.DOTALL)
    #if match:
    #    new_text = f":::{match.group(1)}\n{match.group(3)}\n:::\n\n"
    #    text = text[:match.start()] + new_text + text[match.end():]

    #text = text.replace("GLPI", "i-Vertix ITAM")
    #match = re.sub(r"\{.*?\}", "", text, flags=re.DOTALL)
    #print(match)

    #print(text)

    #with open(f, "w", encoding="utf8") as fd:
    #    fd.write(text)

    ##note = re.search(r"> \[\!(\w+)\]\n(^> .*(\n> .*)*)", text, flags=re.MULTILINE)
    #note = re.search(r"> \[\!(\w+)\]((\n> .*)+)", text, flags=re.MULTILINE)
    #print(note)

    ##note_text = note.group(2).split("\n")
    #note_text = note.group(2).replace("> ", "")
    #print(note_text)



    #match = re.search(r"<div .*>\n\n([\w/\- ]*)\n\n</div>", text, flags=re.MULTILINE)
    #print(text)
    #match = re.search(r"class", text, flags=re.MULTILINE)
    
    #match = re.search(r"::::\s*\n:::\s*\n(.*?):::\n(.*?):::", text, re.DOTALL)
    #print(match)
    #print(match.group(1))
    #print(match.group(2))

    #print(note.group(1))
    #print(note.group(2))
    #print(note)
    
    #match = re.search(r"\.\. toctree::\n\s+:maxdepth: \d+\n\n(.*?)\n\n", text, flags=re.DOTALL)
    #match = re.search(r"\.\. toctree::\n\s+:maxdepth: \d+\n\n(.*?)\n*\Z", text, flags=re.DOTALL)
    #print(match.group(1))
    
    #text = text + "\n\n\n"
    #match = re.search(r"\.\. toctree::\n\s+:maxdepth: \d+\n\s*\n(.*?)\n\n", text, flags=re.DOTALL)
    #match = re.search(r"\.\. toctree::\n\s+:maxdepth: \d+\n\s*\n", text, flags=re.DOTALL)
    
    
    #match = re.search(r"<(http[s]*://.*)>", text)

#    while True:
#
#        match = re.search(r"> \[\!(\w+)\]((\n>.*)+)", text, flags=re.MULTILINE)
#        if not match:
#            break
#
#        print("")
#        print(match)
#        print(text[match.start():match.end()])
#        text = text[match.end():]


match = re.search(r"\s*::::\s*\n\s*:::\s*\n\s*(.*?)\s*:::\n(.*?)\s*::::", text, re.DOTALL)
print(match)