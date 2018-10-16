import math
import time

start = time.time() * 1000.00

is_prime_cache = {}
def is_prime(num):
  if num <= 1:
    return False
  prime = is_prime_cache.get(num)
  if prime == None:
    prime = True
    for i in range(2, int(math.floor(math.sqrt(num)))+1):
      if num % i == 0:
        prime = False
    is_prime_cache[num] = prime
  return prime
    
# find the size of the largest consecutive series of prime numbers that can be produced by f(n)=n^2 + an + b with n starting at zero and define the values of the coeeficients 'a' and 'b' for this case
size_largest_series = 0
function_coefficients_largest_series = [0,0]
for a in range(-999,1000):
  for b in range(-1000,1001):
    n = -1
    prime = True
    while prime:
      n += 1
      prime = is_prime(n**2 + a*n + b)
    if n > size_largest_series:
      size_largest_series = n
      function_coefficients_largest_series[0] = a
      function_coefficients_largest_series[1] = b


print "The function that produced primes for the largest consecutive series was f(n)=n**2 +(" + str(function_coefficients_largest_series[0]) + ")n + (" + str(function_coefficients_largest_series[1]) + ") and it produced prime numbers for the first " + str(size_largest_series) + " integers starting at 0 (0 <= n < " + str(size_largest_series) + ")."
print "The product a * b = " + str(function_coefficients_largest_series[0] * function_coefficients_largest_series[1])
end = time.time() * 1000.00
print "Elapsed time: " + str(end - start) + "ms."

