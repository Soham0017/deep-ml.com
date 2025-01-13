# link to problem : https://www.deep-ml.com/problems/7

import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	if (len(T[0]) != len(A)) or (len(A[0]) != len(S)):
		return -1
		
	A = np.array(A)
	T = np.array(T)
	S = np.array(S)

	if np.linalg.det(T) == 0 or np.linalg.det(S) == 0:
		return -1
	
	inv_T = np.linalg.inv(T)
	transformed_matrix = np.dot(np.dot(inv_T, A), S)
	return transformed_matrix.tolist()

# Examples :
print(transform_matrix([[1, 2], [3, 4]], [[2, 0], [0, 2]], [[1, 1], [0, 1]]))