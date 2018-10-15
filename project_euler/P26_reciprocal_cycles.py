import decimal
import time

start = time.time() * 1000.00


decimal.getcontext().prec = 2000
decimal.getcontext().rounding = decimal.ROUND_FLOOR

def get_recurring_cycle(decimals):
  for i in range(0, len(decimals)/2):
    for y in range(i+1, len(decimals_s)/2):
      possible_cycle = decimals_s[i:y]
      decimals_without_possible_cycle = decimals_s.replace(possible_cycle, "")
      if len(decimals_without_possible_cycle) == 0 or decimals_s.startswith(decimals_without_possible_cycle):
        return possible_cycle
  return ""

longest_recurring_cycle = ""
d = 0
for i in range(2, 1000):
  fraction = decimal.Decimal(1) / decimal.Decimal(i)
  decimals_s = str(fraction)[2:]
  recurring_cycle = get_recurring_cycle(decimals_s)
  if len(recurring_cycle) > len(longest_recurring_cycle):
    d = i
    longest_recurring_cycle = recurring_cycle


print "The longest recurring cycle is: " + longest_recurring_cycle
print "Its length is: " + str(len(longest_recurring_cycle))
print "The divisor of the unit fraction that has this recurring cycle is: " + str(d)
end = time.time() * 1000.00
print "Time elapsesd: " + str(end - start) + "ms"
