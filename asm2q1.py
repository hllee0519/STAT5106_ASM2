import numpy as np

def draw():
	np.random.seed(9527)
	randomNum=np.random.choice(range(1,50), 7, False)
	return (sorted(randomNum[0:6]), randomNum[6])

entry=list(map(int, input("Numbers of your entry: ").strip('[]').split(',')))
draw=draw()
print("Numbers of draw: "+str(draw))
points=0;
for i in entry:
	try:
		entry.index(i)
		print("you cant input duplicate number")
		points=-1;
		break;
	except:
		try:
			draw[0].index(i)
			points+=1
		except:
			if i==draw[1] :
				points+=0.5

# prize=[20, 320, 640, 9600, 157500, 885990, 21531600]
outputMsg="Unit prize of your entry: "
match points:
    case 6:
         outputMsg+="21531600 (1st prize)"
    case 5.5:
         outputMsg+="885990 (2nd prize)"
    case 5:
         outputMsg+="157500 (3rd prize)"
    case 4.5:
        outputMsg+="9600 (4th prize)"
    case 4:
        outputMsg+="640 (5th prize)"
    case 3.5:
        outputMsg+="320 (6th prize)"
    case 3:
        outputMsg+="20 (7th prize)"
    case -1:
    	outputMsg=""

print(outputMsg)

