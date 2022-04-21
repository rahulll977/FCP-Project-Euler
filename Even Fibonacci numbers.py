# 2.Even Fibonacci numbers
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

n = 4000000
count = 0
x = 1  
y = 2  
while x <= n:
    if x % 2 == 0:
        count += x
    x,y = y,x+y 
print(count)
