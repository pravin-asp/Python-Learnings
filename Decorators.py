# Decorator Function 

# Decorator is a function which can extend its function and modify the function.


def decorate_division(fun): # 4
	def innerFunction(n1, n2): # 6
		if n2 == 0: # 7
			return 'Check number 2 value' # 8
		else: # 7
			return fun(n1, n2) # 8
	return innerFunction # 5
		
@decorate_division # 3
def division(n1, n2): # 2 # 9
	return n1 / n2  # 10
	
print(division(100, 0)) # 1 # 8 or 10
