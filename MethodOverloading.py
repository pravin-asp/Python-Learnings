# Method Overloading
# Same method name with different no. of arguments or with different type of arguments in other languages except python

class Test:
	def calculate(self, *n):
		total = 0
		for i in n:
			total += i 
		print(total)
		
t = Test()
t.calculate(10, 20)
t.calculate(10, 20, 30)