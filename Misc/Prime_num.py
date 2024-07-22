n = int(input("Enter an integer:")) 
def is_prime(n): 
	if n == 2: 
		return True 
	for x in range (2, n-1): 
		if n % x == 0: 
			return False 
	return True 
print(is_prime(n))