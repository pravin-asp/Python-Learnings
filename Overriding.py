# Overriding
# same method name in parent and child class is called overriding

# 1. Method Overriding
class Parent:
	def study(self):
		print('Engineering or Medical')
		
class Child(Parent):	
	def play(self):
		print('Playing Kabadi')
		
	def study(self):
		#super().study()
		print('Animation / Director')
		
c = Child()
c.study()

print()
# 2. Constructor Overriding
class Parent:
	def __init__(self):
		print('Parent Class Constructor')
		
	def study(self):
		print('Engineering or Medical')
		
class Child(Parent):	
	def __init__(self):
		#super().__init__()
		print('Child Class Constructor')
		
	def play(self):
		print('Playing Kabadi')
		
	def study(self):
		#super().study()
		print('Animation / Director')
		
c = Child()
c.study()