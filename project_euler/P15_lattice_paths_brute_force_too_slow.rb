# brute force - not the smartest implementation but very quick to come up with
# the problem is: it takes way too long - it's unfeasible.
# but I think it's easier to understand and it works well with small grids. That's why I kept it.
def calculateQtPaths(total, down, right)
  numPaths = 0
  for i in 0..(2**total-1) do
    binary = i.to_s(2).rjust(total, '0')
    if binary.count('0') == down && binary.count('1') == right
	    numPaths += 1
    end
  end
  return numPaths
end

puts calculateQtPaths(40, 20, 20)
