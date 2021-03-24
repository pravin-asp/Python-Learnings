
# Interchanging the keys and values of the dictionary to another dictionary

employees = {'Kathiravan' : 100, 'Viyan' : 101, 'Navilan' : 102, 'Arul' : 103}
employees2 = {}
for keys, values in employees.items():
	#print(keys, values)
	employees2[values] = keys# values added to the dictionary 2
print(employees2)

emp_2 = {values : keys for keys, values in employees.items()}
print(emp_2)

employees = {values : keys for keys, values in employees.items()}
print(employees)



emp = {'Python' : 25000, 'C' : 30000, 'C++' : 40000, 'Java' : 18000}
for lang, sal in emp.items():
	if sal >= 25000:
		print(lang + ' salary is', sal)
	
langList = [lang for lang in emp.keys()]
salList = [sal for sal in emp.values()]
print(langList)
print(salList)

for lang in sorted(emp):
	print(lang, emp[lang])
	
for salary in sorted(emp.values()):
	print(salary)
	
