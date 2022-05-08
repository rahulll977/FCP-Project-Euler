# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

import math

def func(n):
	is_prime = [True]*n
	is_prime[0] = False
	is_prime[1] = False
	for i in range(2,int(math.sqrt(n)+1)):
		index = i*2
		while index < n:
			is_prime[index] = False
			index = index+i
	prime = []
	for i in range(n):
		if is_prime[i] == True:
			prime.append(i)
	return prime


def func_1(n):
	divs = [1]
	for i in range(2,int(math.sqrt(n))+1):
		if n%i == 0:
			divs.extend([i,n/i])
	return list(set(divs))


primes = func(10000)


ami_nums = []


checked = []


for i in range(2,10000):
	if i not in primes and i not in checked:
		da = sum(func_1(i))
		db = sum(func_1(da))
		checked.extend([da,db])
		if i == db:
			if da != db:
				ami_nums.extend([i,da])

                
print ('Sum is {}'.format(sum(ami_nums)))