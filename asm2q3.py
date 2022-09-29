import numpy as np
a = np.asmatrix(np.array([[1 ,2 ,3 ,4 ], [5 ,6 ,7 ,8 ], [9 ,10 ,11 ,12 ], [13 ,14 ,15 ,16 ]]))
b = np.asmatrix(np.array([[4 ,3 ,2 ,1 ], [3 ,6 ,4 ,2 ], [2 ,4 ,6 ,3 ], [1 ,2 ,3 ,4 ]]))
c = np.asmatrix(np.array([[4 ,3 ,2 ,1 ], [5 ,6 ,7 ,8 ], [8 ,7 ,6 ,5 ], [4 ,3 ,2 ,1 ]]))

transposeABC=np.transpose(a*b*c)
transposeCBA=np.transpose(c)*np.transpose(b)*np.transpose(a)
print("tr(ABC) = tr(CAB) = tr(BCA): "+str(np.trace(a*b*c)==np.trace(c*a*b)==np.trace(b*c*a)))
print("(ABC)’ = C’B’A’: "+str(np.array_equal(transposeABC, transposeCBA)))

d = np.identity(4)+a
print("(DB)^-1 = B^-1 * D^-1, where D = I + A−1: "+str(np.allclose(np.linalg.matrix_power(d*b, -1), np.linalg.matrix_power(b, -1)*np.linalg.matrix_power(d, -1))))
# print((np.linalg.matrix_power(d*b, -1)==np.linalg.matrix_power(b, -1)*np.linalg.matrix_power(d, -1)).all())
# print(b.I*d.I)
# print((d*b).I)
# print(b.I*d.I==(d*b).I)

