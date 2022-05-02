# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 21000?

def power(n):
    power = 2
    for x in range(1, n):
        power = 2*power
    return power

def sum(n):
    pow = power(n)
    sum = 0
    while pow > 0:
        modulo = pow%10
        sum = sum + modulo
        pow = pow//10 
    return sum

def main():
    print(int(sum(1000)))

if __name__ == '__main__':
    main()