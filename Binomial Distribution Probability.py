# link to problem : https://www.deep-ml.com/problems/79

import math

def binomial_probability(n, k, p):
	"""
    Calculate the probability of achieving exactly k successes in n independent Bernoulli trials,
    each with probability p of success, using the Binomial distribution formula.
    """
	n_copy = n
	Bin_coef = 1
	cnt = 1
	while n_copy != k: 
		Bin_coef = Bin_coef * n_copy
		Bin_coef = Bin_coef / cnt
		n_copy -= 1
		cnt += 1
	
	res = Bin_coef * ((p)**k ) * ((1-p)**(n-k))
	return round(res, 5)

# Example :
print(binomial_probability(6, 4, 0.7))