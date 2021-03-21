# Program in Python
'''
1 Hour = 100

40 Hours = 40 * 100

Overtime --> 1.5 *  = 150

45 --> 40 * 100 + 150

maximum = 60 Hours only

if he works more than 60 hrs then salary is fixed only upto 60 hrs
'''

hours = int(input("Enter the number of hours worked:"))
money = 100
extra_money = 150
if hours <= 40:
	total = hours * money
	print('Your salary is Rs.%d/-'%total)
else:
	if hours > 60:
		total = 40 * money + 20 * extra_money 
		print('You worked more than 60 hrs and your salary is Rs.%d/-'%total)
	else:
		total = 40 * money + (hours - 40) * extra_money
		print('Your salary is Rs.%d/-'%total)