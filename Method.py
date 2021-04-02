class Customer:
	def deposit(self, amt):
		print('You are going to deposit', amt)
		
name = Customer()
name.deposit(500)

class Test:
	a = 100
	def __init__(self):
		self.b = 200
t = Test()
print(t.b) # 200
print(t.a) # 100
t.a = 777
print(t.a) # 777
print(Test.a) # 100


# In OOPs Function are called as Methods
# Types of Methods
#	--> Instance Method
#		-> Instance - Sample - Memory Reference --> Object
#		-> Instance variables - Object variables - self 
# 	--> Class Method
#	--> Static Method 

# Instance Method or Functions
class Student:
	def __init__(self, name, mark):
		self.name = name
		self.total = mark
	
	def display(self):
		print('Hi', self.name)
		
stu = Student('Python', 450)
stu.display()

# Class Method or Function 
#	--> Inside function definition, only class specific variables(static variables) are only used
#	--> class specific methods - @classmethod --> is a decorator
#	-->	cls variable
#	--> can call class name by using class name or object reference.
class Office:
	noOfHolidays = 10
	@classmethod
	def checkHolidays(cls, branch): # cls is a variable
		print('This year our', branch,'has', cls.noOfHolidays, 'leave')
		
Office.checkHolidays('Chennai')


# Static Method or Function 
#	--> utility method 
# 	--> not instance or class method
#	--> @staticmehtod - is a decorator

class calculator:
	@staticmethod
	def add(n1, n2):
		print('Result is', n1 + n2)
		
a = calculator()
a.add(10, 30)