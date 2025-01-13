# link to problem : https://www.deep-ml.com/problems/6

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	# 2*2 matrix only
	trace = matrix[0][0] + matrix[1][1]
	det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
	disc = ((trace*trace) -(4*det))**0.5
	
	eigenvalues = [(trace + disc)/2, (trace - disc)/2]
	return eigenvalues

# Examples :
print(calculate_eigenvalues([[2, 1], [1, 2]]))