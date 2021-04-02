# Object cannot be present wihtout the class

# This is document string program
# className.(dot)FunctionName
class Student:
	'''This class is about Students''' # documentation string

print(Student.__doc__)
help(Student)


class SuperMarket:
	'''This is my Super Market''' # documentation string is optional

bread = SuperMarket()
bread.brand = 'ABC'
bread.price = 25

biscut = SuperMarket()
biscut.brand = 'DEF'
biscut.price = 10

shampoo = SuperMarket()
shampoo.brand = 'XYZ'
shampoo.price = 5

rice = SuperMarket()
rice.brand = 'Pasmathi'
rice.price = 90

print(rice.price)
print(shampoo.__dict__)# values present in the shampoo object