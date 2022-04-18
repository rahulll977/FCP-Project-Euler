# 2.Even Fibonacci numbers
n = 4000000
count = 0
x = 1  
y = 2  
while x <= n:
    if x % 2 == 0:
        count += x
    x,y = y,x+y 
print(count)