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

for x in range(i):
    for y in range(x+1,i):
        for m in range(len(a[x])):
            match = 0
            for n in range(len(a[y])):
                if a[x][m] == a[y][n]:
                    print(x, m, "   ",y, n)

#print(int((match*2/(len(str)+len(str2)))*100),"% match")