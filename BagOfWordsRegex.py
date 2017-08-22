import glob
import os
import re

def freq(a):
    d = {}
    pattern = '^\w+$'
    for x in a:
        if re.match(pattern,x):
            s = x
        else:
            s = x[:-1]
        d[s] = a.count(x)
    return d

def euclid(arg):
    eucl=0
    for x in arg:
        eucl += arg[x] ** 2
    return eucl

l=[]
eucl=[]
path = "Testfiles\/"
for filename in glob.glob(os.path.join(path, '*.txt')):
    a = open(filename).read().lower().split()
    d=freq(a)
    eucl.append(euclid(d))
    l.append(d)
#Dot product
for i in range(1,len(l)):
    for j in l[i]:
        if j not in l[i-1]:
            pass
print(l)
print(eucl)