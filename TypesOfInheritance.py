# Types of Inheritance

# 1. Single Inheritance 
class HumanBeing:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
class Employee(HumanBeing):
	def __init__(self, name, age, id, sal):
		super().__init__(name, age)
		self.id = id 
		self.salary = sal
	
	def __str__(self):
		return 'Name : {}\nAge : {}\nID : {}\nSalary : {}'.format(self.name, self.age, self.id, self.salary)
		
emp = Employee('Python', 21, 101, 30000)
print(emp) 

# 1. if we print an object, memory reference of an object will be printed --> True
# 2. In python, everything is object --> True
# 3. Hence, if we print anything in python, memory reference will get printed --> False
 
# When ever we try to print an object print statement will internally call str function, whatever is return from the str function will be displayed.


#------------------------------------------------
print()
# 2. Multilevel Inheritance 

class GrandParent:
	def agriculture(self):
		print('Watering plants')
		
class Parent(GrandParent):
	def readingBooks(self):
		print('Reading Books')
		
class Child(Parent):
	def doingExercise(self):
		print('Doing Exercises Regularly')
		
c = Child()
c.doingExercise()
c.readingBooks()
c.agriculture()

#-----------------------------------------
print()
# 3. Hierarchical Inheritance

class Honda:
	def giveSalary(self):
		print('Honda Salary')
		
class Bikes(Honda):
	def designBikes(self):
		print('Honda Bikes')
		
class Cars(Honda):
	def designCars(self):
		print('Honda Cars')
		
emp = Cars()
emp.designCars()
emp.giveSalary()

emp = Bikes()
emp.giveSalary()
emp.designBikes()


#--------------------------------------------
print()
# 4. Multiple Inheritance
# More than one super class is multiple inheritance

class Father:
	def drawing(self):
		print('Father is Drawing')
		
	def goingToJob():
		print('Father is an auditor')

class Mother:
	def goingToJob(self):
		print('Mother is a doctor')
		
class Child(Mother, Father): #class Child(Father, Mother):
	def studying(self):
		print('Child is studying')
		
c = Child()
c.studying()
c.goingToJob()
c.drawing()
Father.goingToJob()

#-----------------------------------------------------
print()
class Parent:
	i = 100
	def __init__(self):
		self.j = 200		# instance variable
		
class C(Parent):
	def m1(self):
		print(super().i)
		print(self.j)
		
c = C()
c.m1()

#-----------------------------------------------------
print()
class Parent:
	i = 100
	def __init__(self):
		self.j = 200		# instance variable
		print('Hi, I am super class consturctor')
		
	def test(self):
		print('Testing in super class')
	
	@staticmethod
	def test2():
		print('Parent static method')
		
	@classmethod
	def test3(cls):
		print('Parent class method')
		
class C(Parent):
	def __init__(self):
		super().__init__()
		super().test()
		super().test2()
		super().test3()
		
	def m1(self):
		print(super().i)
		print(self.j)
		super().test()
		super().test2()
		super().test3()
	
	@classmethod
	def display(cls):
		#super().test()
		#super().test2()
		#super().test3() --- shows error instead
		super(C, cls).test(cls)
		super(C, cls).test2()
		super(C, cls).test3()
		
c = C()
c.m1()
c.display()


# 1. super() --> super class - class level variable, super class -> instance variable
# 2. super() -> from child class constructor and child class instance method, using super() - accessing all types of methods( static, class, instance) in super class.
# 3. From child class, class methods --> accessing parent class instance methods and constructors using super() is not possible.
