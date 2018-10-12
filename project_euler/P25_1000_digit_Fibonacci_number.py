import time

inicio = time.time() * 1000.00

last_fibos = [1,1]

count = 2
curr_fibo = last_fibos[1]
while len(str(curr_fibo)) < 1000:
  last_fibo = last_fibos[1]
  one_before_last_fibo = last_fibos[0]
  curr_fibo = last_fibo + one_before_last_fibo
  last_fibos[0] = last_fibo
  last_fibos[1] = curr_fibo
  count += 1
  
print "Elapsed time: " + str((time.time() * 1000.00) - inicio) + "ms"
print "Result: the index of the first fibonacci number with at least 1000 digits is: " + str(count)
