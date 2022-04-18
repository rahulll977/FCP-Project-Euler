# 1. Multiples of 3 or 5

n = 1000
count = 0
for i in range(1,n):
    if i%3 == 0 or i%5 == 0:
        count += i
print(count)   
