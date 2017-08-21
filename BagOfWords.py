f1=open("Testfiles\/f1.py", "r")
f2=open("Testfiles\/f2.py", "r")
str=f1.read().lower()
str2=f2.read().lower()
a=str.split()
b=str2.split()
match=0
d1={}
d2={}
s=""
for x in a:
    if 123 > ord(x[len(x) - 1]) > 96 or 58 > ord(x[len(x) - 1]) > 47 or ord(x[len(x) - 1]) == 95:
        pass
    else:
        s=x[:-1]
    d1[s]=a.count(x)
for x in b:
    if 123 > ord(x[len(x) - 1]) > 96 or 58 > ord(x[len(x) - 1]) > 47 or ord(x[len(x) - 1]) == 95:
        pass
    else:
        s=x[:-1]
    d1[s]=a.count(x)