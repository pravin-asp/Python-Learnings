def isPhoneNumber(text):
	if len(text) != 10:
		return False
	for i in range(0, 10):	
		if not text[i].isdecimal():
			return False
		if text[0] == '0':
			return False
	return True
	
print(isPhoneNumber('0123456789'))
print(isPhoneNumber('1234567890'))

import re 
def isMobileNumber(sentecne):
	mobileNubmerPattern = re.compile('([0|91][6-9][0-9]{9})')
	#mobileNubmerPattern = re.compile('((0|91)((\d){2, 4}))-([1-9][0-9]{5, 8})')
	#return mobileNubmerPattern.search(sentecne)
	print(mobileNubmerPattern.findall(sentecne))
	return mobileNubmerPattern.findall(sentecne)
	
s = "My mobile number is 916587423654, 09874563210 and 9104285-24242"
result = isMobileNumber(s)
print(type(result))
if result == None:
	print('Number is not present')
else:
	for i in result:
		print(i)
	
# {} - no.of occurrences
# [a-z] - a to z 
# [A-Z] - A to Z 
# [a-cA-C0-9]
# [abcABC]
# {'\d{3}-\d{3}-\d{4}'} 3 digit - 3 digit - 4 digit # 123-456-7890

landline = re.compile('(((91)((\d){2, 4}))-([1-9][0-9]{5, 8}))')
present = landline.search(s)
#print(present.groups())


# Date of Birth Checking
DOB = re.compile(r'([0-3][0-9])/([0-1][0-9])/((\d){4})')
dat = input('Enter your date of birth in dd/mm/yyyy:')
check = DOB.findall(dat)
print(check)
'''
if not check is None:
	print(check.groups())
	date = check.group(1)
	month = check.group(2)
	year = check.group(3)
	print(date, month, year)
	if int(month) in [1, 3, 5, 7, 8, 10, 12]:
		if int(date) > 31:
			print('Invalid date, date can\'t be greater than 31')
		else:
			print('Date of Birth format is correct')
	elif int(month) in [4, 6, 9, 11]:
		if int(date) > 30:
			print('Invalid date, date can\'t be greater than 30')
		else:
			print('Date of Birth format is correct')
	elif int(date) > 29:
		print('Invalid date, date can\'t be greater than 29')
	elif int(date) == 29:
		if not (int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0):
			print('Invalid date, date can\'t be greater than 28')
		else:
			print('Date of Birth format is correct')
else:
	print('Date of Birth format is incorrect')'''
	
# Password Checker

def passwordCheck(password):
	if len(password) < 8:
		print('Password should have 8 characters')
	else:
		if re.search('[a-z]', password) and re.search('[A-Z]', password) and re.search('[0-9]', password):
			print('Strong Password')
		else:
			print('Simple Password')
			
password = input('Enter password:')
passwordCheck(password)

# re module

# 1. match()
# 2. compile()
# 3. findall()
# 4. search()
# 5. sub() --> sub(regex, replacement, target)
# 6. subn()
# 7. fullmatch()
# 8. split()
# 9. finditer()

s = re.sub('[a-z]', '$', 'a1b2c3d4')
print(s)
s = re.subn('[a-z]', '$', 'a1b2c3d4')
print(s)
s = re.split('-', 'Chennai - 6000028')


s = 'tomorrow is our republic day'
result = re.search('^day', s) # starts with day
res = re.search('day$', s) # ends with day 
if result == None:
	print('Not present')
else:
	print('Present')