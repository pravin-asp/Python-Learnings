# Polymorphism - Many forms

print('Hi' + '5')
print(5 + 5)
print('Hi' * 3)
print(5 * 3)

# Operator Overloading
# Method Overloading
# Constructor Overloading

# Inheritance
# Method Overriding
# Constructor Overriding

# Python --> Duck typing Language

class Bike:
	def fill(self):
		print('Fill petrol')
		
class Lorry:
	def fill(self):
		print('Fill Diesel')
		
class Ecar:	
	def fill(self):
		print('Charge')
		
class Vehicles:
	def fill(self):	
		print('Get Ready for ride')
		
def charge(obj):
	obj.fill()
		
b = Bike()
l = Lorry()
c = Ecar()

list = [b, l, c]
for obj in list:
	charge(obj)