# Overloading

# + --> object.__add__(self, another)
# - --> object.__sub__(self, other)
# * --> mul								same as above
# / --> div 
# // --> floordiv
# % --> mod
# ** --> pow 
# += --> iadd
# -= --> isub
# *= --> imul
# /= --> idiv
# //= --> ifloordiv
# < --> lt
# <= --> le 
# > --> gt
# >= --> ge 
# == --> eq
# != --> ne 

class Book:
	def __init__(self, pages):
		self.pages = pages
	
	def __add__(self, another):
		return self.pages + another.pages
		
thirukkural = Book(133)
thiruvasagam = Book(200)
print(thirukkural + thiruvasagam)

# Operator Overloading
print()
class Mobiles:
	def __init__(self, brand, price):
		self.brand = brand
		self.price = price
		
	def __ge__(self, other):
		return self.price >= other.price
		
	def __add__(self, other):
		pass
		

		
		
m1 = Mobiles('Samsung', 100000)
m2 = Mobiles('Apple', 10000)
print(m1 >= m2)

print()
class Mobiles:
	def __init__(self, brand, price, offer):
		self.brand = brand
		self.price = price
		self.offer = offer
		
	def __ge__(self, other):
		return self.price >= other.price
		
	def __add__(self, other):
		return self.offer + other.ccOffer

class CreditCard:
	def __init__(self, brand, ccOffer):
		self.brand = brand
		self.ccOffer = ccOffer

m1 = Mobiles('Samsung', 100000, 1000)
m2 = Mobiles('Apple', 10000, 1000)	
c = CreditCard('Samsung', 500)
print(m1 + c)	





