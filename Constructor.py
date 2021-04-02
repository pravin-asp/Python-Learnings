class SuperMarket:
	'''This is my Super Market'''
	def __init__(self, x, price, discount = None): # Formal Parameters
		self.brand = x
		self.price = price
		self.discount = discount
		print('Check me Check me Check me')
	
bread = SuperMarket('abc', 25, 30) # Actual parameters
biscut = SuperMarket('def', 10, 30)
shampoo = SuperMarket('ghi', 1.5, 30)
#rice = SuperMarket('jkl', 90)

print(bread.price)

# __inti__ is called automatically when the object is created
# __inti__ is called Constructor

# Constructor
#	--> __inti__ is called constructor
# 	--> Special function
#	--> constructor is getting called/ invoked automaticaly whenever we create object.
#	--> Initializing Object specific information

# self --> Object Specific Key Word

rice = SuperMarket('jkl', 90)
print(rice.discount)
print(shampoo.price)

print(biscut.brand)


# Default Constructor --> will be invisible
class student:
	def __init__(self):
		print('Hi I am Default Contructor')
		
name = student()