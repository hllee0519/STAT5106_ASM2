import re
 
line = "Professor Sik-yum Lee assumed the duty of chairman of the Department.";
 
searchObj = re.search( r'(Prof.*? [A-Z]([a-z])+) .*? chair.*? .*?', line, re.M|re.I)
 
if searchObj:
   print("searchObj.group() : ", searchObj.group())
   print( "searchObj.group(1) : ", searchObj.group(1))
else:
   print ("Nothing found!!")