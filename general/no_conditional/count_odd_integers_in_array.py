# from: https://medium.com/@samerbuna/coding-tip-try-to-code-without-if-statements-d06799eed231
#
# Solve the problem without using if-statements (or ternary operators, or switch statements).
#
# Challenge #1: Count the odd integers in an array
# Let’s say we have an array of integers and we want to count how many of these integers are odd.



arrayOfIntegers = [1, 4, 5, 9, 0, -1, 5]

count = 0
for i in arrayOfIntegers:
  count += i % 2

print(count)
