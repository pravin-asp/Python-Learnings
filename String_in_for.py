# No of words present in a sentence

s = 'today is monday'
wordsCount = 1
for letter in s:
	if letter == ' ':
		wordsCount += 1
else:
	print('No of words are ', wordsCount)