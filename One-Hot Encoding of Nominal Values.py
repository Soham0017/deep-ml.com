# link to problem : https://www.deep-ml.com/problems/34

import numpy as np

def to_categorical(x, n_col=None):
	# Assuming n_col >= n and x contains integers
	n = len(set(x))
	if n_col != None:
		n = n_col
	one_hot = np.zeros((len(x), n))
	for i in range(len(x)):
		one_hot[i][x[i]] = 1
	return one_hot

# Example :
print(to_categorical(np.array([3, 1, 2, 1, 3]), 4))