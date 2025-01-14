# link to problem : https://www.deep-ml.com/problems/13

import numpy as np

def determinant_4x4(matrix: list[list[int|float]]) -> float:
	# base case :
	if len(matrix) == 1:
		return matrix[0][0] 

	ans = 0
	matrix = np.array(matrix)

	# recursive case :
	for i in range (len(matrix)):
		minor = np.hstack((matrix[1:, :i] , matrix[1:, i+1:]))
		cofactor = ((-1)**i) * determinant_4x4(minor.tolist())
		ans += matrix[0][i] * cofactor
	
	return ans

# Example :
print(determinant_4x4([[4, 3, 2, 1], [3, 2, 1, 4], [2, 1, 4, 3], [1, 4, 3, 2]]))
