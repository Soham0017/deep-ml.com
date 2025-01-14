# link to problem : https://www.deep-ml.com/problems/14

import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# we have to minimize loss_func
	# loss_func = || y_hat - y ||^2  =  (y_hat - y)^T * (y_hat - y)
	# loss_func = (theta*X - y)^T * (theta*X - y)
	# applying matrix calculas ...
	# (X^T * X)*theta - (X^T * y) = 0
	# theta = ((X^T * X)^(-1)) * ((X^T) * y)
	X = np.array(X)
	Y = np.array(y)
	x_transpose = np.array(list(zip(*X))) # can also use np.transpose
	x_detsq = np.dot(x_transpose, X)
	if np.linalg.det(x_detsq) == 0:
		return -1
	x_detsq_inv = np.linalg.inv(x_detsq)
	theta = np.round(np.dot(np.dot(x_detsq_inv, x_transpose), Y), 4).tolist()

	return theta

# Example :
print(linear_regression_normal_equation([[1, 3, 4], [1, 2, 5], [1, 3, 2]], [1, 2, 1]))