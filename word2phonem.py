
words = []
phonems = []
wordsPhonem = []

with open('listIndonesiaPhonem.txt', 'r') as lines:
	for line in lines:
		phonems.append(line.replace('\n', ''))

with open('wlist','r') as lines:
	for line in lines:
		words.append(line.replace('\n', ''))

for word in words:
	i = 0
	wordPhonem = []
	while i < len(word):
		if (i+1 < len(word)):
			wchar = word[i] + word[i+1]
			if wchar in phonems:
				wordPhonem.append(wchar)
				i += 2
			else:
				wchar = word[i]
				if wchar == 'e':
					if (i-1 >= 0) and  (word[i-1] in ['a', 'e', 'i', 'o', 'u']):
						wordPhonem.append('e')
					else:
						wordPhonem.append('@')
				else:
					wordPhonem.append(wchar)
				i += 1
		else:
			wchar = word[i]
			wordPhonem.append(wchar)

			i += 1
	wordsPhonem.append(wordPhonem)

i=0
with open("indonesiaPronounciation.txt", 'w') as f:
	for phonem in wordsPhonem:
		printPhonem = ''
		for cphonem in phonem:
			printPhonem = printPhonem + cphonem + ' '

		f.write('{}\t\t\t{}\n'.format(words[i].replace('\n', ''), printPhonem))
		i += 1