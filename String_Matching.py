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
    #st = re.sub(r'[^a-z0-9_\n]', '', f.read().lower())
    st=f.read().lower()
    f.close()
    #Directory of files
    file_name = filename.split('\\')
    file=""
    for i in file_name:
        if path.find(i) == -1:
            file += i
    files.append(file)
    directory[file] = st
print(directory)
def LCS(dct1, dct2):
    a,b = dct1.split(),dct2.split()
    match = 0
    for x in a:
        for y in b:
            if x == y:
                if match<len(x):
                    match = len(x)
    return int((match*2/(len(dct1)+len(dct2)))*100)
for i in range(0,(len(files)-1)):
    for j in range((i+1),len(files)):
        try:
            print("Plagiarism between ",files[i],"and ",files[j]," is: ",str(LCS(directory[files[i]],directory[files[j]])),"%")
        except:
            print(files[i]," and ",files[j]," are empty.")