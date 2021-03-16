# Compound Datatypes

# List:
	# List of Objects
	# Grocery List
	
# Group of Objects into a single entity
# Insertion Order is maintained
# Duplicate objects are allowed
# Heterogeneous objects are allowed
# List Objects are mutable.

# List Creation 1
GroceryList = []
print(type(GroceryList), GroceryList) 

# List Creation 2
mark = [100, 45, 56]
print(mark)

# List Creation 3
name = 'python'
l = list(name)
print(l)

# List Creation 4
l = list(range(5))
print(l)

# List Creation 5
s = 'Python is very easy'
list = s.split()
print(list)


# List Creation 6
date = '01-01-1900'
list = date.split()
print(list)
list = date.split('-')
print(list)