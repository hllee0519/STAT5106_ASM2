import numpy as np
import math

def draw():
	np.random.seed(9527)
	randomNum=np.random.choice(range(1,50), 7, False)
	#[5, 11, 19, 20, 40, 45], 44
	return (sorted(randomNum[0:6]), randomNum[6])

def inputChecking(entry):
	if(len(entry)<6):
		return False
	for i in range(len(entry)):
		element = entry[i]
		try:
			if(element>49 or element<0 or entry.index(element)!=i):
				return False
		except:
			continue
	return True

def factorial(n):
	if n<=1:
		return 1
	return n*factorial(n-1)

def combination(n, r):
	return factorial(n)/(factorial(r)*factorial(n-r))

def prizeCal(points, length):
	if points<3:
		return "no prize"
	if(points%1==0):
		for i in range(3, points):
			print(str(i)+" prize: "+str(combination(points, i)*combination(length-points, 6-i)))
		print(str(points)+" prize: "+str(combination(length-points, 6-points)))
	else :
		

	# for i in range(3, math.ceil(points)+1):
	# 	c=combination(length-i, 6-i)
	# 	print(c)

repeat=True
while(repeat):
	entry=list(map(int, input("Numbers of your entry: ").strip('[]').split(',')))
	if(inputChecking(entry)==False):
		print("you must input 6 number from 1 to 49 without repetition")
	else:
		repeat=False

draw=draw()
print("Numbers of draw: "+str(draw))
points=0;

for i in entry:
	try:
		draw[0].index(i)
		points+=1
	except:
		if i==draw[1] :
			points+=0.5

prizeCal(points, len(entry))
#[3, 11, 19, 20, 41, 44, 46]


# prize=[20, 320, 640, 9600, 157500, 885990, 21531600]
# outputMsg="Unit prize of your entry: "
# match points:
#     case 6:
#          outputMsg+="21531600 (1st prize)"
#     case 5.5:
#          outputMsg+="885990 (2nd prize)"
#     case 5:
#          outputMsg+="157500 (3rd prize)"
#     case 4.5:
#         outputMsg+="9600 (4th prize)"
#     case 4:
#         outputMsg+="640 (5th prize)"
#     case 3.5:
#         outputMsg+="320 (6th prize)"
#     case 3:
#         outputMsg+="20 (7th prize)"
#     case -1:
#     	outputMsg=""

# print(outputMsg)

