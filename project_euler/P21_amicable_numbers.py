# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

def d(n):
    sum_divisors = 0
    for i in range(n/2):
        if n % (i+1) == 0:
            sum_divisors += (i+1)
    return sum_divisors

# upper limit
n = 10000

# find amicable numbers under the upper limit
amicable_numbers = set()
for i in range(n):
    num = i+1
    d_num = d(num)
    d_d_num = d(d_num)
    if num != d_num and num == d_d_num:
        amicable_numbers.add(i+1)
        amicable_numbers.add(d_num)

# show the result 
print sum(amicable_numbers)

