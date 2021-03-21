'''d = eval(input('Enter dictionary:'))
print(d)
print(type(d))'''


# Getting items for dictionary at run time 
'''register = {}
while True:
	roll = input('Enter your roll no:')
	name = input('Enter your name')
	register[roll] = name
	nextCandidate = input("Enter No to stop : ")
	if nextCandidate == 'No':
		break
print(register)'''

prices = {'apple' : 100, 'grapes' : 200, 'banana' : 50, 'orange' : 60}
for prodName, prodPrice in prices.items():
	print(prodName, '-->', prodPrice)
