f1=open("Testfiles\/f1.txt", "r")
f2=open("Testfiles\/f2.txt", "r")
str=f1.read().lower()
str2=f2.read().lower()
a=str.split()
b=str2.split()
print(a,b)
max=0
for y in b:
    if str.find(y)!=-1:
        max+=len(y)
print(max)