# Constructor Overloading

class SuperMarket:
	def __init__(self, *content):
		print("Constructor Check")
		
obj1 = SuperMarket(10, 20, 30)
obj2 = SuperMarket(30)