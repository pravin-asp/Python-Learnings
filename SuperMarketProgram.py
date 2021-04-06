class SuperMarket:
	__items = []
	__quantity_ava = []
	__price = []
	__cus_items = []
	__cus_qua = []
	
	def load(self):
		self.load_quantity = int(input('Enter the quantity of Load Came:'))
		for iter in range(self.load_quantity):
			self.item = input('Enter the item name:')
			self.quantity = int(input('Enter the item quantity:'))
			self.money = int(input('Enter the amount:'))
			if self.item not in self.__items:
				self.__items.append(self.item)
				self.__quantity_ava.append(self.quantity)
				self.__price.append(self.money)
			print()
		print()
	
	def Quantity_Available(self): 
		print('----------------------Stock Available--------------------------')
		print('S.No\tItems\tQuantity\tPrice')
		for iter in range(self.load_quantity):
			print('{}\t{}\t{}\t{}'.format(iter, self.__items[iter], self.__quantity_ava[iter], self.__price[iter]))
		print('---------------------------------------------------------------')
		print()
		
	def Customer_Load(self):
		print('----------------------Customer\'s Load-------------------------')
		choice = 'y'
		self.quan = 0
		while choice == 'y':
			self.item = input('Item Name:')
			self.quantity = int(input('Item Quantity:'))
			if self.item not in self.__cus_items:
				self.__cus_items.append(self.item)
				self.__cus_qua.append(self.quantity)
				self.__quantity_ava[self.__items.index(self.item)] = self.__quantity_ava[self.__items.index(self.item)] - self.quantity 
			choice = input('Enter y to continue:')
			self.quan += 1
		print()
		
	def Invoice(self):
		self.total = 0
		print('-------------------------Invoice------------------------------')
		print('S.No\tItems\tQuantity\tPrice')
		for iter in range(self.quan):
			print('{}\t{}\t{}\t{}'.format(iter, self.__cus_items[iter], self.__cus_qua[iter], self.__cus_qua[iter] * self.__price[self.__items.index(self.__cus_items[iter])]))
			self.total += self.__cus_qua[iter] * self.__price[self.__items.index(self.__cus_items[iter])]
		print('\t\tTotal:\t', self.total)
		print('---------------------------------------------------------------')
		print()
		
if __name__ == "__main__":
	shop = SuperMarket()
	shop.load()
	shop.Quantity_Available()
	shop.Customer_Load()
	shop.Invoice()
	shop.Quantity_Available()