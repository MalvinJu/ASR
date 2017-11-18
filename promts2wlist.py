import re
import pickle

regexAlphabet = re.compile("[^a-zA-Z-]+")

def getKey(item):
	return item[0]

def prompts2wlist(files):
	wlist = []

	for file in files:
		with open(file,'r') as lines:
		    prompts = [line.strip().split('\t') for line in lines]

		i = 0
		for prompt in prompts:
			j=0
			wordsPronounce = prompt[2].split(' ')
			for word in prompt[1].split(' '):
				regexWords = regexAlphabet.sub('', word)
				regexWordsPronounce = regexAlphabet.sub('', wordsPronounce[j])
				# check for empty string
				if regexWords != '':
					# split word contain '-' ex.'hilang-hilangan'
					splitWords = regexWords.split('-')

					if (len(splitWords) > 2):
						if (splitWords[0] != splitWords[1]):
							wlist.append((regexWords, regexWordsPronounce))
						else:
							splitWordsPronounce = regexWordsPronounce.split('-')
							wlist.append((splitWords[0], splitWordsPronounce[0]))
					else:
						wlist.append((regexWords, regexWordsPronounce))
				j += 1
			i += 1
						

	# unique and sorted
	wlist = sorted(list(set(wlist)), key=getKey)
	#wlist = sorted(list(set(wlist)))
	return wlist

""" MAIN PROGRAM """
with open('listPrompts.txt','r') as lines:
	files = [line.strip() for line in lines]

wlist = prompts2wlist(files)

wlistUnique = []
for wordTuple in wlist:
	wlistUnique.append(wordTuple[0])
wlistUnique=sorted(list(set(wlistUnique)))

with open("wlist", 'w') as f:
	for word in wlistUnique:
		f.write("{}\n".format(word))

with open("wlistPronounce", 'w') as f:
	for word in wlist:
		f.write("{}\t{}\n".format(word[0], word[1]))
