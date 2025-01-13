# link to problem : https://www.deep-ml.com/problems/5

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	result = [[ele * scalar for ele in row] for row in matrix]
	return result

# Example :
print(scalar_multiply([[1,2],[3,4]], 2))
