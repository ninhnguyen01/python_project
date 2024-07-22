def savings(p, i, t): 
	return p * (1 + i)**t 
p = float(input("Enter current bank balance:")) 
i = float(input("Enter interest rate:")) 
t = float(input("Enter the amount of time that passes:")) 
print(savings(p, i, t))