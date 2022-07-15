a=input()
a=a.lower()
c=[]
e=[]
d=''
for i in a:
    if i!=" ":
        c.append(i)
c=set(c)
e=list(c)
e.sort()
for i in e:
    d+=i
print(d)    