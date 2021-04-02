# static 

# self variables ( Object Specific Variables)
#	--> multiple copies will be maintained

# Class Specific Variables
#	--> Only one copy will be maintained

class SuperMarket:
	'''This is my Super Market'''
	manufacturer = 'Python Learning'
	marketer = 'Python.org'
	def __init__(self, x, price, discount = None): # Formal Parameters
		self.brand = x
		self.price = price
		self.discount = discount
		print('Check me Check me Check me')
	
bread = SuperMarket('abc', 25, 30) # Actual parameters
biscut = SuperMarket('def', 10, 30)
shampoo = SuperMarket('ghi', 1.5, 30)
rice = SuperMarket('abc', 10)


rice.manufacturer = 'TAPCMS'

print(SuperMarket.manufacturer)
print(SuperMarket.marketer)

print(rice.manufacturer)
print(shampoo.manufacturer)