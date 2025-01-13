# link to problem : https://www.deep-ml.com/problems/2

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	row = len(a)
	col = len(a[0])
	b = []
	for i in range(col):
		temp = []
		for j in range(row):
			temp.append(a[j][i])
		b.append(temp)
	return b

# Example :
print(transpose_matrix([[1,2],[3,4],[5,6]]))