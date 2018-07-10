# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

n = 100

# calculate the factorial
factorial_n = 1
for i in range(100):
    factorial_n = factorial_n * (i+1)

# break the result into an array of chars and sum up the numbers
factorial_digit_array = list(str(factorial_n))
factorial_digit_sum = 0
for s in factorial_digit_array:
    factorial_digit_sum += int(s)

# show the result
print factorial_digit_sum
