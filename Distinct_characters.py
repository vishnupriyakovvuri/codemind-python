a=input()
a=a.lower()
c=[]
e=[]
d=''
for i in a:
    if i!=" " and a.count(i)==1:
        c.append(i)
c=set(c)
e=list(c)
e.sort()
for i in e:
    d+=i
print(d)    