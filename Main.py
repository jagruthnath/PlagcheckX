f1=open("Testfiles\/f1.py", "r")
f2=open("Testfiles\/f2.py", "r")
str=f1.read()
str2=f2.read()
a=str.split()
b=str2.split()
match=0
for x in a:
    for y in b:
        if x==y:
            match+=1
print(int((match/(len(b)+len(a)))*100),"% match")