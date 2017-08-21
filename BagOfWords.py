import tkinter.dialog
import tkinter
st=""
window = tkinter.Tk()
window.minsize(width=500,height=300)
def buttonCallBack():
    window.file = tkinter.dialog.(initialdir="/", title="Select file",filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
def printCallBack():
    print( sim*100 , "% match")
t1=tkinter.Entry(window).grid(row=0,column=1)
t2=tkinter.Entry(window).grid(row=1,column=1)

b1 = tkinter.Button(window, text ="Browse File 1 ...", command = buttonCallBack)
b2 = tkinter.Button(window, text ="Browse File 2 ...", command = buttonCallBack)
b3 = tkinter.Button(window, text ="Check for plagiarism", command = printCallBack)

l1=tkinter.Label(window, text="File 1 : ").grid(row=0)
l2=tkinter.Label(window, text="File 2 : ").grid(row=1)

b1.grid(row=0,column=2)
b2.grid(row=1,column=2)

b3.grid(row=2,column=1)

window.mainloop()

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
for x in d1:
    dp += ( d1[x] * d2[x] )
sim = dp / ( eu1 * eu2 )
print( sim*100 , "% match")