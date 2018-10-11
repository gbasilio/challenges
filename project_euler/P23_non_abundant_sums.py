import math
import time

start = int(round(time.time() * 1000))

# find abundant numbers
abundant = []
for i in range(1,28123):
  divisors = [1]
  # find divisors
  for j in range(2, int(round(math.sqrt(i)))+1):
    if i % j == 0:
        if (i/j == j):
          divisors.append(j)
        else:
          divisors.append(j)
          divisors.append(i/j)
  #check abundance
  if sum(divisors) > i:
      abundant.append(i)


# find all integers smaller or equal to 28123 that can be written as a sum of 2 abundant numbers
sum_of_2_abundants = {}
for i in range(0,len(abundant)):
    for y in range(i,len(abundant)):
        sum_abundant = abundant[i] + abundant[y]
        sum_of_2_abundants[sum_abundant] = 1
        if sum_abundant >= 28123:
          break


# find the sum of all the integers smaller or equal to 28123 that can't be written as a sum of 2 abundant numbers
result = 0
for i in range(1,28124):
    if sum_of_2_abundants.get(i) == None:
      result += i

end = int(round(time.time() * 1000))

print "Time elapsed: " + str(end - start) + "ms"
print "Result: " + str(result)
  
