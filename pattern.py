import glob
import os
import re
path = "Testfiles\/"
a,st = [],[]
nof=0
for filename in glob.glob(os.path.join(path, '*.txt')):
    st.append(open(filename).read().lower())
    st=re.sub(r'[^a-z0-9_\n]', '', st)
    a.append(st[nof].split())
    nof+=1

f = []
def prefix(p):
    m = len(p)
    for x in range(m):
        f.append(0)
    i,j = 1,0
    while i<m:
        if p[i] == p[j]:
            f[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            j = f[ j - 1 ]
        else:
            f[i] = 0
            i += 1
def kmp(t,p):
    prefix(p)
    n = len(t)
    i,j = 0,0
    while i < n:
        if t[i] == p[j]:
            if j == m - 1:
                return i - j
            else:
                i += 1
                j += 1
    else:
            if j > 0:
                j = f[ j - 1 ]
            else:
                i += 1
    return -1
t = input("Enter text : ")
n = len(t)
p = input("Enter pattern : ")
m = len(p)
pos=kmp(t,p)
if pos==-1:
    print("Pattern not found!")
else:
    print("Pattern found at position ",pos+1)