import math

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
        s = x
    else:
        s=x[:-1]
        print(s)
    d1[s] = a.count(x)
    d2[s] = 0
for x in b:
    if 123 > ord(x[len(x) - 1]) > 96 or 58 > ord(x[len(x) - 1]) > 47 or ord(x[len(x) - 1]) == 95:
        s = x
    else:
        s = x[:-1]
    d2[s] = b.count(x)
    if s not in d1:
        d1[s]=0
eu1=0
eu2=0
for x in d1:
    eu1 += d1[x]**2
for x in d2:
    eu2 += d2[x]**2
dp=0
print(d1,d2)
for x in d1:
    dp += ( d1[x] * d2[x] )
    print(dp)
sim = dp / ( eu1 * eu2 )
print( sim*100 , "% match")