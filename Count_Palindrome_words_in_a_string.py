a=input()
a=a.lower()
c=[]
d=0
b=''
for i in a:
    if (i!=" "):
        b+=i
    else:
        c.append(b)
        b=''
c.append(b)
for i in c:
    if i==i[-1::-1]:
        d+=1
print(d)        