# link to problem : https://www.deep-ml.com/problems/64

import numpy as np

def gini_impurity(y):
	n = len(y)
	freq = dict()

	for cl in y:
		if cl in freq:
			freq[cl] += 1
		else:
			freq[cl] = 1

	sq_sum = 0
	for i in freq:
		sq_sum += (freq[i] / n)**2

	return np.round(1-sq_sum, 3)

# Example :
y = [0, 0, 0, 0, 0, 1] 
print(gini_impurity(y))