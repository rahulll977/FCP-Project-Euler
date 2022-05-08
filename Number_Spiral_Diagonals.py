"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

last_number = 1001*1001


odd_numbers = range(1,last_number+1,2)


i = 0


gap = 1

solution = 1

while odd_numbers[i] != last_number:
	for j in range(4):
		i+= gap
		solution += odd_numbers[i]
	gap += 1

print (solution)