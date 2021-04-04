# Exception Handling

# Error:

# Syntax Error and Exception is different

# print(10 / 0) this is an exception


'''try:
	n1 = int(input())
	n2 = int(input())
	print(n1 / n2)	# risky code
except ZeroDivisionError:
	print('Check It seems like zeor in denominator')
except ValueError:
	print('Check the numbers')
print('Hi')'''

# Runtime Error --> Exception

# In python, Everything is Object

# whenever exception occurs, the corresponding exception object will give / throw to the end user

# Object - memory reference of a class / instance of a class

# 1. Every Exception in python is a class
# 2. All Exception classes are child / Sub classes of BaseException class
# 3. During runtime, if exception occurs, Python will throw us the exception class name and stops the program immediately / abruptly.


# Exception Handling
'''
def division():
	try :
		a = int(input())
		b = int(input())
		print(a / b)
	except ValueError:	# Handling code
		print('Something went wrong')
		#division()
	except:
		print('An Error Occured')
		#division()
	finally:		# cleanup code
		print('Check I am in finally')
		

division()
'''
# Nested Exception Handling
try:
	a = int(input())
	b = int(input())
	try:
		print(a / b)
	except ZeroDivisionError:
		print('Zero is in the denominator')
	finally:
		print('Inner Finally')
except ValueError:
	print('Check the numbers')
finally:
	print('Outer Finally')

# Using else in try and except
print()
try:
	print('Try Block')
	print(int(input())/ int(input()))
except:
	print('Exception Occurs')
else:		# Else part gets executed when no except
	print('Else part')
finally:
	print('In Finally')
	
	
# User Defined Exception
'''class InsufficientBalanceException(Exception):	
	def __init__(self):
		print('Check your balacne')
	
balance = 1000
amount = int(input('Enter amount to withdraw:'))
if amount > balance:
	raise InsufficientBalanceException()
	
'''
class InsufficientBalanceException(Exception):	
	def __init__(self, message):
		#self.msg = message
		pass
	
balance = 1000
amount = int(input('Enter amount to withdraw:'))
if amount > balance:
	raise InsufficientBalanceException('Check your balance')
	
'''class InsufficientBalanceException(Exception):	
	def __init__(self, msg):
		self.msg = msg

try:		
	balance = 1000
	amount = int(input('Enter amount to withdraw:'))
	if amount > balance:
		raise InsufficientBalanceException('Check your balance')
except InsufficientBalanceException:
	print('Insufficient Balance in your Account')
	print('Enter an amount less than your balance in multiples of 100')'''