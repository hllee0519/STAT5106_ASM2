import numpy as np
a=np.array([[3,2],[0,1]])
b=np.array([[-2,0],[1,1]])

aM=np.matrix('3 2;0 1')
bM=np.matrix('-2 0;1 1')

aP=np.linalg.inv(a)
bP=np.linalg.inv(b)
abP=np.linalg.inv(b*a)

print(bP*aP)
print(abP)
print(bP*aP==abP)
print(np.array_equal(abP,bP*aP))

aP=np.linalg.inv(aM)
bP=np.linalg.inv(bM)
abP=np.linalg.inv(aM*bM)
print()
print(np.linalg.inv(bM)*np.linalg.inv(aM))
print(np.linalg.inv(aM*bM))
print(bP*aP==abP)
print(np.array_equal(abP,aP*bP))