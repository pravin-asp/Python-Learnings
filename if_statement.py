# Control Flow Statements

mark = 90
#if statement
if mark >= 90:
	print('Very Good')

	
#if else statement 	
if mark >= 90:
	print('Very Good')
else:
	print('Good')
	
#elif statement 
mark = int(input('Enter a mark:'))
if mark > 90:
	print('90+')
elif mark > 80:
	print('80+')
elif mark > 70:
	print('70+')
else:
	print('We are in same boat')
	

#Nested if statement 	
total = int(input('Enter total:'))
if total > 400:
	tamil = int(input('Enter tamil mark:'))
	if tamil > 80:
		print('Very great')
	else:
		print('Nice')
else:
	print('Ok, thanks')