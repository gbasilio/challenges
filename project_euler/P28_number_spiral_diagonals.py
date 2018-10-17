import time

start = time.time() * 1000.00

diagonal_numbers = [1]
last_diagonal_number = 1
diagonal_increment = 2
for i in range (3,1002,2):
    for y in range(0,4):
        curr_diagonal_number = last_diagonal_number + diagonal_increment
        diagonal_numbers.append(curr_diagonal_number)
        last_diagonal_number = curr_diagonal_number
    diagonal_increment += 2

print "The sum of the numbers in the diagonal of a 1001 by 1001 spiral is : " + str(sum(diagonal_numbers))
end = time.time() * 1000.00
print "Elapsed time: " + str(end - start) + "ms."
