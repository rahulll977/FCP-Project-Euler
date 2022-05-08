"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
def Prime(n):
    if n == 2 or n == 3 or n == 5: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    if n%5 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: 
            return False
        if n%(f+2) == 0: 
            return False
        f +=6
    return True

def gen(nb):
    results = []
    nb_str = str(nb)
    for k in range(0, len(nb_str) - 1):
        results.append(nb_str[k:])
        results.append(nb_str[-k:])
    return results

def check(nb):
    for t in gen(nb):
        if not Prime(int(t)):
            return False
    return True

c = 0
s = 0
i = 2
while c != 11:
    if check(i):
        c += 1
        s += i
    i += 1
print(s)