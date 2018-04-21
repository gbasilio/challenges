triangulo =[
[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 04, 82, 47, 65],
[19, 01, 23, 75, 03, 34],
[88, 02, 77, 73, 07, 63, 67],
[99, 65, 04, 28, 06, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 04, 23]]


# len(triangulo)-2: because dont want to process the last line - each value is already the maximum to the bottom
# triangulo)-2, -1: it ends in -1 because range function in python doesn't include the end value so I have to define the end as -1 if I want it to go to 0. I'll never get used to python's range not including the end! That's so counter intuitive to me. :-)
for i in range(len(triangulo)-2, -1, -1):
  for j in range(0, i+1):
    triangulo[i][j] = triangulo[i][j] + max(triangulo[i+1][j], triangulo[i+1][j+1])

print triangulo[0][0]

