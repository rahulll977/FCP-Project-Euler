# 1. Multiples of 3 or 5
# Find the sum of all the multiples of 3 or 5 below 1000.

n = 1000
count = 0
for i in range(1,n):
    if i%3 == 0 or i%5 == 0:
        count += i
print(count)   
