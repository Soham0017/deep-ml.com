# link to problem : https://www.deep-ml.com/problems/8

import numpy as np

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
	if np.linalg.det(matrix) == 0:
		return None
	inverse = np.round(np.linalg.inv(matrix), 3).tolist()
	return inverse

# Example :
print(inverse_2x2([[4, 7], [2, 6]]))