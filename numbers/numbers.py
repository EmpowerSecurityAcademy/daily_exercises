
# write a function that sums all multiples of 3 and 5
# below a certain number
def sum_3_5_multiples(ceiling_number):
	total = 0
	for num in range(ceiling_number):
		if num % 3 == 0 or num % 5 == 0:
			total += num
	return total


#find the sum of all fibonacci numbers below 1,000,000
def sum_fibonacci_numbers_below_1000000():
	fibonaccis = []
	current = 1
	previous = 1
	while current < 1000000:
		holder = current
		current += previous
		fibonaccis.append(previous)
		previous = holder
	fibonaccis.append(previous)
	total = 0
	for num in fibonaccis:
		total += num
	return total


def palindrome_checker(possible_palindrome):
	string_length = len(possible_palindrome)
	for i, character in enumerate(possible_palindrome):
		if possible_palindrome[(string_length - i - 1)] != character:
			return False

	return True

#largest palindrome product
#palindrome number is the same forward and backwards
#find the largest palindrome number that is the product of two three digit numbers
#example for two digit 9009 = 91 * 99
def largest_palindrome_of_thee_digit_numbers():
	highest_sum = 0
	for  x in range(100, 999):
		for y in range(100, 999):
			multiple = x * y
			if palindrome_checker(str(multiple)):
				if multiple > highest_sum:
					highest_sum = multiple
	return highest_sum




