# filter()

l = [2, 3, 4, 22, 37, 42, 59, 72, True, False]

def even(n):
	if n % 2 == 0:
		return True
	else:
		return False

evenlist = filter(even, l)
print(*evenlist)


evenlist = filter(None, l)
print(*evenlist)

evenlist = filter(lambda x : x % 2 != 0, l)
print(*evenlist)


# map()
def km(m, ms):
	return m * 1.6, ms * 1.6
	
mile = [3, 4, 5, 6]
miles = [7, 8, 9, 10]
#k = map(km, mile)
#print(list(k))
k = map(lambda x : x * 1.6, mile)
print(list(k))

k = map(km, mile, miles)
print(list(k))


# reduce()
from functools import reduce # reduce --> reduces the sequence of elements into a single element
product = reduce((lambda x, y : x * y), [1, 2, 3, 4])
print(product)

from functools import *
result = reduce((lambda n1, n2 : n1 + n2), range(1, 101))
print(result)

'''
how to create package of our own:

before adding any package first initialise that folder
with __init__.py to consider that folder as package by the python

then how to access that package

folderName.fileName
or
folderName.subFolderName.fileName
'''