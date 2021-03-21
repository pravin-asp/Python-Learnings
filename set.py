# SET : Mathematical Set

# No duplicates allwoed
# No order is maintained
# Set objects are mutable

# List --> []
# Tuple --> ()
# Set --> {}

# Set no index 
# no slicing

# Intersection
# Union
# Difference

s = {30, 50, 10, 20, 30}
print(s)
print(list(s))
print(tuple(s))
s = set(range(10))
print(s)

l = list()
print(type(l))
t = tuple()
print(type(t))
s = {} 
print(type(s))# dictionary
s = set()
print(type(s))
l = []
print(type(l))
t = ()
print(type(t))

name = 'python'
l = list(name)
print(l)
t = tuple(name)
print(t)
s = set(name)
print(s)

# add function
s.add(4500)
print(s)

# Update function
s = {10, 20, 30, 40, 50}
l = [100, 200, 300, 400, 500]
s.update(l)
print(s)

s.update(l, range(5))
print(s)

# copy()
s2 = s.copy()
print(s2)

# pop() --> random value will be removed from the set only for the set 
print(s2.pop())
print(s2)

# remove(a) --> removes a particular value
s.remove(400)
print(s)

# discard(a) --> removes a particular value
s.discard(300)
print(s)

# if we use s.remove(100000) shows error
# if we use s.discard(100000) not shows error 

# set --> does not support indexing and slicing 

# Union function
s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}
print(s1.union(s2)) # or 
print(s1 | s2)
 
# Intersection function
print(s1 & s2)
print(s1.intersection(s2))

# Difference function
print(s1 - s2)
print(s1.difference(s2))
print(s2 - s1)
print(s2.difference(s1))

# Symmetric difference function
print(s1 ^ s2)

# Frozen set --> immutable set 
f = frozenset(s1)
print(f)
