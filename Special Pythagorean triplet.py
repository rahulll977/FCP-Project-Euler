#9.Special Pythagorean Triplet

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#  a2 + b2 = c2
#  For example, 32 + 42 = 9 + 16 = 25 = 52.
#  There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#  Find the product abc.




def func():
	peri = 1000
	for a in range(1, peri + 1):
		for b in range(a + 1, peri + 1):
			c = peri - a - b
			if a * a + b * b == c * c:
				return str(a * b * c)


if __name__ == "__main__":
	print(func())
