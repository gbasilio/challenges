# using combinatorics the problem gets much easier to compute
# p = n! / k! * (n - k)! => choosing 20 out of 40 
# but it also gets more cryptic as one can't get the logic from reading the code - one has to study a bit of combinatorics to understand what is going on

def factorial(n)
  (1 .. n).reduce(:*)
end

def combinations(total, chosenQt)
  factorial(total) / (factorial(chosenQt) * factorial(total - chosenQt))
end

puts combinations(40, 20)

