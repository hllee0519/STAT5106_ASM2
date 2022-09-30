import re
enigma=[['7', ' ', '3'],
		['T', 's' ,'i'],
		['h', '%' ,'x'],
		['i', ' ' ,'#'],
		['s', 'M' ,' '],
		['$', 'a' ,' '],
		['#', 't' ,'%'],
		['i', 'r' ,'!']]
# enigma=[['7 3'],
# 		['Tsi'],
# 		['h%x'],
# 		['i #'],
# 		['sM '],
# 		['$a '],
# 		['#t%'],
# 		['ir!']]
# enigma="7 3\nTsi\nh%x\ni #\nsM \n$a \n#t%\nir!";

rearange=""
i=0
for i in range(0, len(enigma[i])):
	for n in range(1, len(enigma)):
		rearange+=enigma[n][i]
print(rearange)
pattern = re.compile(r'\w*([\W|\s]*)\w+', re.I)
f=pattern.findall(rearange)
print(f)
for ele in f:
	rearange=" ".join([rearange[:rearange.index(ele)], rearange[rearange.index(ele)+len(ele):]])
print(rearange)