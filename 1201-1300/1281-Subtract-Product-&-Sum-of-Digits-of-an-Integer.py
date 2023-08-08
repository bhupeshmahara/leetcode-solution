# time O(n)
# space O(n)


class Solution:
	def subtractProductAndSum(self, n: int) -> int:
		product_of_digits = 1
		sum_of_digits = 0
		n_str = str(n) # convert the integer n to string for easy digit extraction
		for digit_char in n_str:
			digit = int(digit_char) # convert the string back to integer
			product_of_digits *= digit
			sum_of_digits += digit
		difference = product_of_digits - sum_of_digits
		return difference


from functools import reduce
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a = [int(x) for x in str(n)]
        return reduce((lambda x, y: x * y), a) - reduce((lambda x, y: x + y), a)


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sums = 0
        while n != 0:
            last = n % 10
            prod *= last
            sums += last
            n =n//10
        return prod - sums
