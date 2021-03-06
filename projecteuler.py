#Problem 1
def sum_multof3and5(n):
	z = 0
	for x in range(1,n):
		if x % 3 == 0 and x % 5 != 0:
			z = z + x
	for y in range(1,n):
		if y % 5 == 0:
			z = z + y
	print z
#sum_multof3and5(1000)
#Problem1 -- Alternative Solution
def sum_multof3and5_alternative(n):
	print sum(x for x in xrange(n) if not (x % 3 and x % 5)) 
#As long as x is not divisble by both 3 and 5, but still divisible 
#by either 3 or 5, take it and add all existing values of x
#It's interesting how this is observed with De Morgan's law: ~(P ^ Q) is the same as ~P v ~Q
#sum_multof3and5_alternative(1000)
#Problem 2
def sum_of_even_fibonacci_numbers():
	x = 1
	y = 2
	z = x + y
	a = []
	a.append(y)
	while z < 4000000:
		x = z + y
		y = x + z
		z = x + y
		if x % 2 == 0:
			a.append(x)
		if y % 2 == 0:
			a.append(y)
		if z % 2 == 0:
			a.append(z)
	print sum(a)
#sum_of_even_fibonacci_numbers()
#Problem 3
import math
def largest_prime_factor(n):
	e = 2
	while e < int(math.sqrt(n)):
		if n % e == 0:
			n = n / e
		e = e + 1
	print n
#largest_prime_factor(600851475143)
#Problem 4 
def largest_palindrome_product_of_two3digitnumbers():
	a = 0
	for x in range(1,999):
		for y in range(1,999):
			z = x * y
			if z > a:
				b = str(z)
				if b == b[::-1]: #slices a string such that it reads it backwards
					a = z
	print a
#largest_palindrome_product_of_two3digitnumbers()
#Problem 5
def smallest_multiple(n):
	e = n
	a = 2
	while n % a == 0:
		a += 1
	b = a
	while b < n:
		if e % b != 0:
			e += n
			b = a
		else:
			b += 1
	print a	
smallest_multiple(20) 
