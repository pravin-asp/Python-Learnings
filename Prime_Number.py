n = int(input())
div = 2
while div < n:
	if n % div == 0:
		print("Not prime")
		break
	div += 1
else:
	print("Prime")