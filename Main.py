f1=open("Testfiles\/f1.txt", "r")
f2=open("Testfiles\/f2.txt", "r")
str=f1.read()
str2=f2.read()
print(str,str2)
a=str.split()
b=str2.split()
match=0
for x in a:
    for y in b:
        if x==y:
            match=len(x)
print(int((match*2/(len(str)+len(str2)))*100),"% match")