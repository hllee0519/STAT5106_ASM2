import re

for line in open("dept_hist.html", "r",encoding="utf-8"):  # opened in text-mode; all EOLs are converted to '\n'
    line = line.rstrip('\n')
    searchObj = re.search( r'.*?(Prof.*? [^A-Z][a-z$]+).*?chair.*?.*?', line, re.M)
    if searchObj:
        print(searchObj.group(1))