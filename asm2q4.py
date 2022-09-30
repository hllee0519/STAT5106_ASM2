import re

for line in open("dept_hist.html", "r",encoding="utf-8"):  # opened in text-mode; all EOLs are converted to '\n'
    line = line.rstrip('\n')
    searchName = re.search( r'(Prof\.|Professor)\s([A-Z][a-z]+[-a-z]+|[A-Z][a-z]+)\s([A-Z][a-z]+\s[A-Z][a-z]+|[A-Z][a-z]+) .*? chair.*?', line)
    searchName2 = re.search( r'.*? chair.*? (Prof\.|Professor)\s([A-Z][a-z]+[-a-z]+)\s([A-Z][a-z]+\s[A-Z][a-z]+|[A-Z][a-z]+) ', line)
    try:
        print(searchName.group(1), end=' ')
        print(searchName.group(2), end=' ')
        print(searchName.group(3))
    except:
        continue