# link to problem : https://www.deep-ml.com/problems/10

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:

	# n : no. of features, covariance matrix will be of n * n size
	n = len(vectors) 
	m = len(vectors[0])

	# matrix of means of each feature
	means = [sum(row) / m for row in vectors]

	ans = []
	for i in range(n):
		temp = []
		for j in range(n):
			# calculate covariance for feature_i and feature_j
			cov = sum((vectors[i][k] - means[i]) * (vectors[j][k] - means[j]) for k in range(m)) / (m-1)
			temp.append(cov)
		ans.append(temp)
		
	return ans

# Examples :
print(calculate_covariance_matrix([[1, 5, 6], [2, 3, 4], [7, 8, 9]]))