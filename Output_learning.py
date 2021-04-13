a, b, c = 100, 200, 300
print(a, b, c)
print(a, b, c, sep = ' : ')#at each and every space of output it works 
print(a, b, c, end = ' - ')#at the end only it works


#Formatted String
# %i --> int 
# %d --> int 
# %f --> float 
# %s --> string 
print()
a, b, c = 100, 200.09, 'Pravin'
print('a value %d'%a)
print('b value is %f and c is %s'%(b, c))

name = 'Pravin'
print('Welcome %s to my home'%name)



#Replacement Operator

name = 'Pravin'
city = 'Tiruchengode'
print('Hi this is {}. I am from {}'.format(name, city))
print('Hi this is {0}. I am from {1}'.format(name, city))
print('Hi this is {1}. I am from {0}'.format(name, city))

name = input('Enter your name : ')
print('lenght of name is %d'%len(name))
mid = len(name) // 2
print(name[: mid] + name[mid].upper() + name[mid + 1 :])


print(__file__) # to print file name 

import os
print(os.path.abspath(__file__)) # gives the absolute path 


print(os.path.dirname(os.path.abspath(__file__))) # gives the directory location alone
