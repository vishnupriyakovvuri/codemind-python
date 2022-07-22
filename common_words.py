a=input()
b=input()
a=a.lower()
b=b.lower()
a=a.split(" ")
b=b.split(" ")
c=[]
d=[]
e=[]
for i in a:
        c.append(i)
for i in b:
        e.append(i)
for i in c:
    e.append(i)
for i in e:
    if e.count(i)>1:
        if i not in d:
            d.append(i)
print(*d)            