names = ['stephen', 'muthu', 'celin', 'rajarajan']

time = [18, 22.3, 19.1, 17.2]

for i in range(3):
	for j in range(i + 1, 4):
		if time[i] > time[j]:
			time[i], time[j] = time[j], time[i]
			names[i], names[j] = names[j], names[i]

for i in range(len(names)):
	print(names[i], time[i])
	
a = '10+20+30'
print(eval(a))