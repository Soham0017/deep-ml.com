# link to problem : https://www.deep-ml.com/problems/77

def performance_metrics(actual: list[int], predicted: list[int]) -> tuple:
	# Implement your code here
	tp, tn, fp, fn, n = 0, 0, 0, 0, len(actual)
	for i in range(n):
		if actual[i] == predicted[i] == 1:
			tp += 1
		elif actual[i] == predicted[i] == 0:
			tn += 1
		elif actual[i] == 0:
			fp += 1
		else:
			fn += 1
	
	confusion_matrix = [[tp, fn], [fp, tn]]
	accuracy = (tp + tn) / n

	precision = tp / (tp + fp) # labelled pos out of actually pos
	negativePredictive = tn / (tn + fn) # labelled neg out of actually neg
	recall = tp / (tp +fn) # correctly labelled out os all pos
	specificity = tn / (tn +fp) # correctly labellrd out of all neg

	# f1 : harmonic mean of precision and recall
	f1 =  2 * (precision * recall) / (precision + recall)

	return confusion_matrix, round(accuracy, 3), round(f1, 3), round(specificity, 3), round(negativePredictive, 3)

# Example :
actual = [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1]
predicted = [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0]
print(performance_metrics(actual, predicted))
