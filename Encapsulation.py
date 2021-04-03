# Encapsulation --> Data Binding

# public
# private
# protected 
# the above 3 key words not in python

# protected --> within the same and inherited classes
# protected --> _

class Test:
	a = 100 # public variable
	_b = 200 # protected variable
	__c = 300 # private variable
	
	def __init__(self):
		self.__no = 1234
		
	def display(self):
		print(Test.a)
		print(Test._b)
		print(Test.__c)
		print()
		
t = Test()
t.display()
print(t.a)
print(t._b)
# print(t.__c) shows error
