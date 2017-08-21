f1=open("Testfiles\j1.txt", "r")
f2=open("Testfiles\j2.txt", "r")
str=f1.read()
str2=f2.read()
a=str.split()
b=str2.split()
match=0
for x in a:
    for y in b:
        if x==y:
            match+=1
print((match/len(b))*100,"% match")