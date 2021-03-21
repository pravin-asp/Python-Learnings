#Dictionary
'''
Key - Value Pair

Train Time Table

Nellai Exp = 1900
Pandian Exp = 2000
KK Exp = 2100
Vaigai Exp = 2100


Exam Time Table
tamil - 21032021
'''


# No duplicate keys allowed
# Values can be duplicates
# No insertion order is maintained
# Dictionaries are mutable
# No indexing, slicing

d = {}
print(type(d))

d[1234] = 'celin'
d[1235] = 'Ilangoven'
d[1236] = 'Ilangoven'
print(d)

d = {1234 : 'C', 1235 : 'C++', 1236 : 'Java', 1237 : 'Pyton', 1238 : 'C#'}
print(d)
d[1235] = 100
print(d)
d[200] = 'Python'
print(d)

# del --> used to delete the key and value 

del d[1235]
print(d)

# clear() --> removes all the values in the dictionary

# del --> entirely delets the dictionary from the entry

print(len(d))

# get(key) --> used to get value of the that key
print(d.get(1236))
print(d[1236])

print(d.get(12345)) # gives value as none
#print(d[12345]) # shows error

# pop(key must be present) --> removes the value from the dictionary
d.pop(1234)#removes the key and value
print(d)

# item --> key, value pair
# dictionary items or dictionary contains 4 items


#popitem() --> randomly removes the key value pairs from the dictionary
print(d.popitem())
print(d)

for i in d:
	print(d[i])

# to get all keys of the dictionary
print(d.keys())
print(type(d.keys()))

# to get keys of the dictionary
for key in d.keys():
	print(key)
for key in d:
	print(key)
#d = {}
# to get values of the dictionary
for value in d.values():
	print(value)
for value in d:
	print(d[value])
	
# to get the item of the dictionary
for item in d.items():
	print(item)
print(d.items())

# copy() --> copies the value to another dictionary
d1 = d.copy()
print(d1)
d[1] = 'Pravin'
# update()
d1.update(d)
print(d1)

print(d.get(2))
print(d.get(12, 'Not Available'))