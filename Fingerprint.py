import glob
import re
import os

lst = []
directory = {}
files = []
path = "Testfiles\/"

for filename in glob.glob(os.path.join(path, '*.txt')):
	#File reading
	f = open(filename,'r')
	l = re.sub(r'[^a-z0-9_\n]', '', f.read().lower())
	f.close()
	#Directory of files
	file_name = filename.split('\\')
	file=""
	for i in file_name:
		if path.find(i) == -1:
			file += i
	files.append(file)
	directory[file] = l
print(directory)

def lcs(S,T):
	m = len(S)
	n = len(T)
	counter = [[0]*(n+1) for x in range(m+1)]
	longest = 0
	length=0
	for i in range(m):
		for j in range(n):
			if S[i] == T[j]:
				c = counter[i][j] + 1
				counter[i+1][j+1] = c
				if c > longest:
					longest = c
					length=len(S[i-c+1:i+1])
				elif c == longest:
					length=len(S[i-c+1:i+1])
	return (2*length/(len(S)+len(T)))*100
#Comparing all the lists of files.
for i in range(0,(len(files)-1)):
	for j in range((i+1),len(files)):
		try:
			print("Plagiarism between ",files[i],"and ",files[j]," is: ",str(lcs(directory[files[i]],directory[files[j]])),"%")
		except:
			print(files[i]," and ",files[j]," are empty.")
	print()