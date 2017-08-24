import readFile
readFile.read_file()
files=readFile.files
lst=readFile.lst
directory=readFile.directory
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
	return int((2*(length-1)/(len(S)+len(T)))*100)
#Comparing all the lists of files.
for i in range(0,(len(files)-1)):
	for j in range((i+1),len(files)):
		try:
			print("Plagiarism between ",files[i],"and ",files[j]," is: ",str(lcs(directory[files[i]],directory[files[j]])),"%",)
		except:
			print(files[i]," and ",files[j]," are empty.")
	print()