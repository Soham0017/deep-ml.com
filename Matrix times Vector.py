# link to problem : https://www.deep-ml.com/problems/1

import numpy as np

def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	if len(a[0]) != len(b):
		return -1
	c = []
	for i in range(len(a)):
		c.append(np.dot(a[i], b))
	return c

# Example:
print(matrix_dot_vector([[1,2,3],[2,4,5],[6,8,9]],[1,2,3]))