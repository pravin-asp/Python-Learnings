import sys
class Customer:
	'''This is Customer of SBI'''
	bankName = 'State Bank of India'
	
	def __init__(self, name, accNo, balance = 0):
		self.name = name
		self.accNo = accNo
		self.balance = balance
	
	def deposit(self, amount):
		self.balance = self.balance + amount
		print('Your balance is Rs.', self.balance)
		
	def withdraw(self, amount):
		if amount > self.balance:
			print('Insufficient Balance')
		else:
			self.balance -= amount
		print('Your balance is Rs.', self.balance)
		
print('Welcome to', Customer.bankName)
name = input('What is your name?')
accNo = int(input('Enter your account no.:'))
customer1 = Customer(name, accNo)

while True:
	print('D - Deposit, W - Withdraw, S - Stop')
	choice = input('Enter your choice:')
	if choice == 'D':
		amount = int(input('Enter amount:'))
		customer1.deposit(amount)
	elif choice == 'W':
		amount = int(input('Enter amount:'))
		customer1.withdraw(amount)
	elif choice == 'S':
		sys.exit()