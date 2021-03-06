#Read files from directory code start
import readFile
readFile.read_file()
files=readFile.files
lst=readFile.lst
directory=readFile.directory
#Read files from directory code end

#Pattern matching code start
def LCS(dct1, dct2):
    a,b = dct1.split(),dct2.split()
    match = 0
    for x in a:
        if 123 > ord(x[len(x) - 1]) > 96 or 58 > ord(x[len(x) - 1]) > 47 or ord(x[len(x) - 1]) == 95:
            s = x
        else:
            s = x[:-1]
        for y in b:
            if 123 > ord(y[len(y) - 1]) > 96 or 58 > ord(y[len(y) - 1]) > 47 or ord(y[len(y) - 1]) == 95:
                r = y
            else:
                r = y[:-1]
            if s == r:
                if match<len(s):
                    match = len(s)
    return int((match*2/(len(dct1)+len(dct2)))*100)
#Pattern matching code end

#Main code for checking plagiarism start
"""print("Filename",end="  ")
for x in files:
    print(x,end="  ")
print()
for x in files:
    print(x)"""
#Calculation for two files at a time
for i in range(0,(len(files)-1)):
    for j in range((i+1),len(files)):
        try:
            print("Plagiarism between ",files[i],"and ",files[j]," is: ",str(LCS(directory[files[i]],directory[files[j]])),"%")
        except:
            print(files[i]," and ",files[j]," are empty.")
    print()
#Main code for checking plagiarism start