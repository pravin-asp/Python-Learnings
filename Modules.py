# Modules --> file / folder
	#Put necessary files in a folder is called modules
	
# Code Reusability

# Abstraction --> Showing only necessary data and hiding unwanted one.

# Eg : Car --> Accelerator, Gear, Clutch, Brake
				# Showing only the fuctionality not the code
				
# If we want to use modules we have to use import 
'''
import math
print(math.factorial(5))
print(math.floor(5.2))
print(math.ceil(5.2))
print(int(math.pow(5, 3)))'''

# Group of functions, variables and classes
import add
#print(add.num)
print(add.add())
print(add.sub())
print(add.add() * add.sub())

# Module Aliasing

import add as a 
print(a.add())

print()
# only specific function from the modules
from add import sub 
print(sub())

from add import add 
print(add())

print()
import add as a
print(a.add())
print(a.sub())

from add import * # * --> all members present in add modules
print(add())
print(sub())# dont want to give a.add() or add.add() just add() alone is enough

import add
#print(dir()) # dir() --> discreption about the modules and what are the functions are available
print(dir(add))
print('Program:',__name__)
# __name__ :
# modules.py --> python program --> __name__ ==> __main__
# add.py --> module 