class Details:
	def __init__(self, name, cPlay, age, cBlg):
		self.name = name
		self.cPlay = cPlay
		self.age = age
		self.cBlg = cBlg
		
def findPlayer(P_Details):
	count = 0
	for pd in P_Details:
		if len(pd.cPlay) > count:
			count = len(pd.cPlay)
			person = pd.name
	return person
	
def countCountry(P_Details, country):
	count = 0
	for pd in P_Details:
		if pd.cBlg.lower() == country.lower():
			count += 1
	return count
	
if __name__ == "__main__":
	players = int(input('Enter the number of Players:'))
	P_Details = []
	for player in range(players):
		name = input('Enter the player name:')
		countries = []
		plyCou = int(input('Enter the no.of countries played:'))
		for country in range(plyCou):
			print('Enter country %d:'%country)
			countries.append(input())
		age = int(input('Enter the player age:'))
		cBlg = input('Enter the player Country:')
		P_Details.append(Details(name, countries, age, cBlg))
	country = input('Enter the country to count:')
	print(countCountry(P_Details, country))
	print(findPlayer(P_Details))
			