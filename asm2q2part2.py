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
		n=0
		for i in range(3, points):
			print(str(6-n)+" prize: "+str(combination(points, i)*combination(length-points, 6-i)))
			n+=1
		print(str(points)+" prize: "+str(combination(length-points, 6-points)))
	else:
		print(str(points)+" prize: "+str(combination(length-math.ceil(points), 6-math.ceil(points))))
		for i in range(int((points-0.5)*2), 5, -1):
			if((i/2)%1==0):
				print(str(i/2)+" prize: "+str(combination(math.floor(points), i/2)*combination(length-math.ceil(points), 6-i/2)))
			else:
				print(str(i/2)+" prize: "+str((combination(math.ceil(points), math.ceil(i/2))*combination(length-math.ceil(points), 6-math.ceil(i/2)))-(combination(math.floor(points), math.ceil(i/2))*combination(length-math.ceil(points), 6-math.ceil(i/2)))))

# main start
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

