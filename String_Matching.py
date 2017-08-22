import glob
import os
path = "Testfiles\/"
a,st = [],[]
i=0
for filename in glob.glob(os.path.join(path, '*.txt')):
    st.append(open(filename).read().lower())
    a.append(st[i].split())
    i+=1

print(i)
print(st)
print(a)
match=0
ar=[]
"""
for x in range(len(a)):
    for y in range(len(a[x])):
        match = 0
        for z in range(len(a[x])):
            if a[x][y] == a[x][z]:
                print(x,y,"   ",x,z)
                match += 1
        ar.append(match)
    del ar[len(ar) - 1]"""
print(ar)

#print(int((match*2/(len(str)+len(str2)))*100),"% match")