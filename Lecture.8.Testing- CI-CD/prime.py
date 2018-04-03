import math

def is_prime(n):
	""" Determines if a non-negative interger is prime."""
	if n < 2:
		return False
	for i in range(2, int(math.sqrt(n) + 1)):
		if n % 1 == 0:
			return False
	return True