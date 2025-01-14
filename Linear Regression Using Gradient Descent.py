# link to problem : https://www.deep-ml.com/problems/15

import numpy as np
def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:

	m, n = X.shape
	theta = np.zeros((n, 1))
	for it in range(iterations):
		pred = np.dot(X, theta) # pred.shape = m * 1 
		err = pred - y.reshape(m, 1) # err.shape = m * 1
		updates = (np.dot(X.T, err)) / m #updates.shape = n * 1
		theta -= alpha * updates

	return np.round(theta.reshape(1, n), 4)

# Example :
print(linear_regression_gradient_descent(np.array([[1, 1], [1, 2], [1, 3]]), np.array([1, 2, 3]), 0.01, 1000))