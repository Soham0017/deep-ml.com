# link to problem : https://www.deep-ml.com/problems/9

import numpy as np

def matrixmul(a:list[list[int|float]], b:list[list[int|float]])-> list[list[int|float]]:
	if len(a[0]) != len(b):
		return -1		  
	return np.dot(a,b)

# Example :
print(matrixmul([[1,2,3],[2,3,4],[5,6,7]],[[3,2,1],[4,3,2],[5,4,3]]))