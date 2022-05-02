# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    limit = int(n ** 0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

def next_prime(count_limit):
    yield 2
    count = 1
    n = 3
    while True:
        if is_prime(n):
            yield n
            count += 1
            if count == count_limit:
                return
        n += 2

n = 10001

# Good
item = None
for item in next_prime(n):
    pass
print(item)
