# Inheritance 
#	--> Object of one class behaving as object of another class

# HAS-A relationship  # Raja has a book
					  # Raja - class, book - class 
# IS-A relationship   # Lion is a Animl
						
						
# Composition HAS-A Relationship
class Engine:
	mileage = 15
	
	def __init__(self):
		self.petrol = True 
	
	def engineStart(self):
		print('Engine Starting')
		
class Car:
	def __init__(self):
		self.engine = Engine()
		
	def drive(self):
		print(self.engine.mileage)
		self.engine.engineStart()
		
swift = Car()
swift.drive()



# Aggregation IS-A Relationship
# Lion is a Animal
# Raja is Human Being

class RBI:
	name = 'Reserve Bank of India'
	def __init__(self):
		self.minBalance = 2000
		
	def deposit(self):
		print('Deposit in RBI')
		
	def withdraw(self):
		print('Withdraw in RBI')
		
	@staticmethod
	def f1():
		print('RBI Static Method')
		
	@classmethod
	def f2(cls):
		print('RBI Class Method')
		
class SBI(RBI):
	pass

tgode = SBI()
tgode.deposit()
tgode.withdraw()
tgode.f1()
tgode.f2()


class VasanthAndCo: # Parent class or Super class 
	address = 'vadapalani'
	def __init__(self):
		self.ho_offer = 1000
		
class VasanthAndCoMadurai(VasanthAndCo): # Child class or Sub class 
	adres = 'Madurai'
	def __init__(self):
		super().__init__()
		self.br_offer = 500

customer = VasanthAndCoMadurai()
print(customer.br_offer)
print(customer.ho_offer) # Throws an error if super() is not given
print(customer.address)


class HumanBeing:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def readingBooks(self):
		print('Reading Books')
		
class Employee(HumanBeing):
	def __init__(self, name, eno, salary):
		super().__init__(name, 21)
		self.name = name
		self.eno = eno
		self.salary = salary
		
	def doWork(self):
		print('Working')
		
	def getEmployeeDetails(self):
		print(self.name)
		print(self.eno)
		print(self.salary)
		print(self.age)

emp1 = Employee('Raja', 101, 10000)
emp1.doWork()
emp1.getEmployeeDetails()
emp1.readingBooks()


# Types of Inheritance:

# Core Idea --> Code Reusability

# 1. Single Inheritance --> above example
# 2. Multilevel Inheritance --> below example


class ReserveBank:
	def deposit(self):
		print('deposit')
		
	def withdraw(self):
		print('withdraw')
		
class StateBank(ReserveBank):
	def giveEducationLoan(self):
		print('education loan')
		
class CooperativeBank(StateBank):
	def giveAgriLoan(self):
		print('Agri Loan')
		
village = CooperativeBank()
village.giveAgriLoan()
village.giveEducationLoan()
village.deposit()
village.withdraw()

# Hirareical Inheritance
class ReserveBank:
	def deposit(self):
		print('deposit')
		
	def withdraw(self):
		print('withdraw')
		
class StateBank(ReserveBank):
	def giveEducationLoan(self):
		print('education loan')
		
class IndianBank(ReserveBank):
	def giveEducationLoan(self):
		print('education loan in Indian Bank')
		
class CooperativeBank(StateBank):
	def giveAgriLoan(self):
		print('Agri Loan')
		
tgode = IndianBank()
tgode.giveEducationLoan()