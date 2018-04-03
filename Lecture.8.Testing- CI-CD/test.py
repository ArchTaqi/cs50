from prime import is_prime


def test_prime(n, expected):
	if is_prime(n) != expected:
		#print(f"ERROR on is_prime({n}), expected {expected}")
		print("ERROR")

# test via bash script
"""
python3 -c "from prime import is_prime: test_prime(1, False)"
"""

def square(x):
	return x * x


#assert square(10) == 1000
# to get exit code of program echo $? , if return 1 means last promram exit with sone error, if 0 then last program exit with success.



##############################################################################################
########################## Playing with Unittests ############################################

import unittest2

class Tests(unittest2.TestCase):

	def test_1(self):
		""" Check that 1 is not the prime """
		self.assertFalse(is_prime(1))

	def test_2(self):
		""" Check that 1 is not the prime """
		self.assertFalse(is_prime(2))

	def test_8(self):
		""" Check that 8 is not the prime """
		self.assertFalse(is_prime(8))

	def test_11(self):
		""" Check that 11 is not the prime """
		self.assertFalse(is_prime(11))

	def test_25(self):
		""" Check that 25 is not the prime """
		self.assertFalse(is_prime(25))

	def test_28(self):
		""" Check that 28 is not the prime """
		self.assertFalse(is_prime(28))								

if __name__ == "__main__":
    unittest2.main()