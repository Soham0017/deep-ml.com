# link to problem : https://www.deep-ml.com/problems/4

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	m = len(matrix)
	n = len(matrix[0])
	means = []
	if mode == 'column':
		for i in range(n):
			temp = (sum(matrix[j][i] for j in range(m))) / m
			means.append(temp)
	else:
		for i in range(m):
			temp = (sum(matrix[i][j] for j in range(n))) / n
			means.append(temp)
	return means

# Examples :
print(calculate_matrix_mean([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 'column'))