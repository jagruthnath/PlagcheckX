import readFile
readFile.read_file()
files=readFile.files
lst=readFile.lst
directory=readFile.directory
def euclid(arg):
    eucl=0
    for x in arg:
        eucl += arg[x] ** 2
    return eucl

def freq(a,b):
    d1,d2 = {},{}
    for x in a:
        if 123 > ord(x[len(x) - 1]) > 96 or 58 > ord(x[len(x) - 1]) > 47 or ord(x[len(x) - 1]) == 95:
            s = x
        else:
            s = x[:-1]
        d1[s] = a.count(x)
        d2[s] = 0
    for x in b:
        if 123 > ord(x[len(x) - 1]) > 96 or 58 > ord(x[len(x) - 1]) > 47 or ord(x[len(x) - 1]) == 95:
            s = x
        else:
            s = x[:-1]
        d2[s] = b.count(x)
        if s not in d1:
            d1[s] = 0
    return [d1,d2]
for i in range(0,(len(files)-1)):
    for j in range((i+1),len(files)):
        try:
            a = directory[files[i]].split()
            b = directory[files[j]].split()
            s = ""
            d1 = freq(a, b)[0]
            d2 = freq(a, b)[1]
            eu1 = euclid(d1)
            eu2 = euclid(d2)
            dp = 0
            for x in d1:
                dp += (d1[x] * d2[x])
            sim = dp / (eu1 * eu2)
            print("Plagiarism between ",files[i],"and ",files[j]," is: ",sim * 100, "%")
        except:
            print(files[i]," and ",files[j]," are empty.")
    print()