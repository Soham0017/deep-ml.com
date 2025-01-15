# link to problem : https://www.deep-ml.com/problems/16

import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):

	maxi = np.max(data, axis = 0)
	mini = np.min(data, axis = 0)
	mean = np.mean(data, axis = 0)
	std = np.std(data, axis = 0) 

	standardized_data = np.round((data - mean) / std, 4).tolist()
	normalized_data = np.round((data - mini) / (maxi - mini), 4).tolist()

	return standardized_data, normalized_data

# Example :
print(feature_scaling(np.array([[1, 2], [3, 4], [5, 6]])))



