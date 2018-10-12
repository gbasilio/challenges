import time

def permute(param_set, start_index, end_index, permutations):
  local_set = list(param_set) # we want to work with a local set so that invocations of the function permute don't interfere with one another
  if start_index == end_index:
    permutations.append(''.join(local_set))
  else:
    for i in range(start_index, end_index+1):
      local_set[start_index], local_set[i] = local_set[i], local_set[start_index]
      permute(local_set, start_index+1, end_index, permutations)



inicio = time.time() * 1000.00

string = "0123456789"
permutations = []
permute(list(string), 0, len(string)-1, permutations)
permutations.sort()


print "Elapsed time: " + str((time.time() * 1000.00) - inicio) + "ms"

print "Result: the one millionth lexicographic permutation is: " + permutations[999999]

