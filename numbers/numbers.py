
# write a function that sums all multiples of 3 and 5
# below a certain number
def sum_3_5_multiples(ceiling_number):
	total = 0
	for num in range(ceiling_number):
		if num % 3 or num % 5:
			total += num
	return total


#find the sum of all fibonacci numbers below 1,000,000
def sum_fibonacci_numbers_below_1000000():
	



#largest palindrome product
#palindrome number is the same forward and backwards
#find the largest palindrome number that is the product of two two digit numbers
#example 9009 = 91 * 99
#def largest_palindrome_of_thee_digit_numbers():
