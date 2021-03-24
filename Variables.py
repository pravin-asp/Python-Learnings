# Local Variable
# Global Variable

discount = 20 # Global Variable

def openingTime():
	global discount
	discount = 30
	print(discount)
	
def purchaseTV():
	print(discount)
	
def purchaseLapTop():
	discount = 25 # Local Variable
	print(globals()['discount'], discount)
	
openingTime()
purchaseTV()
purchaseLapTop()

list = [1, 3, 5, 7, 9]
Double_digit_odd_num = []
for i in range(len(list)):
	for j in range(len(list)):
		Double_digit_odd_num.append(list[i] * 10 + list[j])
print(Double_digit_odd_num)