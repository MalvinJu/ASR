import re
import os

regexAlphabet = re.compile("[^a-zA-Z-]+")

def readSetMapping(file):
	with open(file,'r') as lines:
		mapping = [line.strip().split(' ') for line in lines]

	return mapping

def readTranscript(file):
	transcript = []

	with open(file,'r') as lines:
	    prompts = [line.strip().split('\t') for line in lines]

	for prompt in prompts:
		transcript.append((prompt[0], prompt[1]))
						
	return transcript

def checkMapping(setMapping, name):
	mapping = ""
	for item in setMapping:
		if item[1] == name:
			mapping = item[0]
			break

	return mapping

def checkTranscript(transcripts, recordName):
	transcript = ""
	for item in transcripts:
		if item[0][2:5] == recordName:
			transcript = item[1]
			break

	return transcript

# Main Program
setMapping = readSetMapping("MAPPING_TO_TRANSCRIPT")
dirTuple = list(os.walk("DIRECTORY_AUDIO"))
setsDir = dirTuple[0][1]

mlf=[]
i=1
for setDir in setsDir:
	print(setDir)
	transcriptName = checkMapping(setMapping, setDir) + "-raw.tsv"
	print(transcriptName)
	transcripts = readTranscript(transcriptName)
	
	for recordName in dirTuple[i][2]:
		mlf.append((recordName, checkTranscript(transcripts, recordName[10:13])))
	i+=1

with open("words.mlf", 'w') as f:
	f.write("#!MLF!#\n")
	for transcriptMLF in mlf:
		f.write("\"*/{}.lab\"\n".format(transcriptMLF[0]).replace(".wav", ""))
		for word in transcriptMLF[1].strip().split(' '):
			f.write("{}\n".format(regexAlphabet.sub('', word).upper()))
		f.write(".\n")

	