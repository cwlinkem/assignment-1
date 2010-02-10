#will break a number into its prime factors

num = input ("Please enter a number: ")



def calc_factors(num):
	small_factors = []
	i = 2
	while i <= num:
		if num % i == 0:
			small_factors = calc_factors(num/i)
			small_factors.append(i)
			return small_factors
		i += 1
	factors = small_factors
	factors.sort()
	return factors

factors = calc_factors(num)
print 'The number', str(num), 'can be factored into the following prime numbers',factors


