# Abstraction

# Showing only the necessary data and hiding the unwanted.

# ABC --> Abstract Base Class

from abc import *	
class Indian(ABC):
	@abstractmethod
	def havingBreakFast(self):
		pass

class Tamils(Indian):
	def havingBreakFast(self):
		print('Eating Pongal, vada, idli')
		
class Marati(Indian):	
	def havingBreakFast(self):
		print('Chapati')
		
t = Tamils()
#t.havingBreakFast()

# Abstract Class --> Class with at least one abstract method.
		
# if we extend/ inherit abstract class and we don't override the abstract methods present in parent class, In that case, Child Class is also considered as abstract and we couldn't instantiate(create object) for child class as well.


# Interfaces

# --> there is no interface in python
# --> if all the methods are abstract then it is called Interfaces

from abc import *

class DBInterface(ABC):
	@abstractmethod
	def establishDB(self):
		pass
		
	@abstractmethod
	def disconnectDB(self):
		pass
		
class OracleDB(DBInterface):
	def establishDB(self):
		print('Oracle DB Connection')
		
	def disconnectDB(self):
		print('Oracle DB disconnection')
		
class MySQLDB(DBInterface):
	def establishDB(self):
		print('MySQL DB Connection')
		
	def disconnectDB(self):
		print('MySQL DB disconnection')
		
dbName = input('Enter DB name:')
className = globals()[dbName] # globals()[str] --> converts the string into its class name object
c = className()
c.establishDB()
c.disconnectDB()	