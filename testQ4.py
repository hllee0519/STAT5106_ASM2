import re
 
lines = ["Professor Sik-yum Lee assumed the duty of chairman of the Department.", 
   "Professor Nai Ng Chan became the third chairman of the Department.",
   "Foundation of the Department. 17 students were enrolled in the first year with Prof. Howell Tong as the chairman",
   "Professor Qi Man Shao was inaugurated as the Department chairman"];
 
for line in lines:
   searchObj = re.search( r'(Prof\.|Professor)\s([A-Z][a-z]+[-a-z]+|[A-Z][a-z]+)\s([A-Z][a-z]+\s[A-Z][a-z]+|[A-Z][a-z]+) .*? chair.*?', line)

   try:
      print( "searchObj.group() : ", searchObj.group())
      print( "searchObj.group(1) : ", searchObj.group(1))
      print( "searchObj.group(2) : ", searchObj.group(2))
      print( "searchObj.group(3) : ", searchObj.group(3))
      print( "searchObj.group(4) : ", searchObj.group(4))
   except:
      continue