#!/usr/bin/python

# With the computer power we have at our disposal these days the simplest way to solve this problem is by brute force. But we have to find an 
# upper bound if we dont't want to run forever. To do that we have to find the largest number that can be represented by fifth powers 
# where the number of digits is greater than or equal to the number of elements of the sum.
#
# 1 digit: 9^5 = 59049
# 2 digits: 2 * 9^5 = 118098
# 3 digits: 3 * 9^5 = 177147
# 4 digits: 4 * 9^5 = 236196
# 5 digits: 5 * 9^5 = 295245 
# 6 digits: 6 * 9^5 = 354294
# 7 digits: 7 * 9^5 = 413343
#
# By the values above we can see that the largest number we can represent by fifth powers where the number of digits is greater than or equal
# to the number of elements of the sum is 354294 (6 digit number formed by a sum of 6 powers). We can't form a 7 digit number by the sum of
# 7 fifth powers, neither 8, or 9 and so on. Thus 354294 is our upper bound.

numbers_sum_of_fifth_power_of_digits = []

for i in range(1,354295):
    digits = list(str(i))
    fifth_power_sum = 0
    for digit in digits:
        fifth_power_sum += int(digit)**5
        if fifth_power_sum > i:
            break
    if fifth_power_sum == i and i != 1:
        numbers_sum_of_fifth_power_of_digits.append(i)



print "The sum of all the numbers that can be written as the sum of fifth powers of their digits is: " + str(sum(numbers_sum_of_fifth_power_of_digits))
print "The numbers are: " + str(numbers_sum_of_fifth_power_of_digits)
