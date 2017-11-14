import re
import pickle

regexAlphabet = re.compile("[^a-zA-Z-]+")

def prompts2wlist(files):
	wlist = []

	for file in files:
		with open(file,'r') as lines:
		    prompts = [line.strip().split('\t') for line in lines]

		for prompt in prompts:
			for word in prompt[1].split(' '):
				regexWords = regexAlphabet.sub('', word)
				# check for empty string
				if regexWords != '':
					# split word contain '-' ex.'hilang-hilangan'
					regexWords = regexWords.split('-')
					for regexWord in regexWords:
						wlist.append(regexAlphabet.sub('', regexWord))

	# unique and sorted
	wlist = sorted(list(set(wlist)))
	return wlist

""" MAIN PROGRAM """
with open('listPrompts.txt','r') as lines:
	files = [line.strip() for line in lines]

wlist = prompts2wlist(files)

with open("wlist", 'w') as f:
	for word in wlist:
		f.write("%s\n" % word)


