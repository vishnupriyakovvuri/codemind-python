a=input()
a=a.lower()
b=''
k=''
c=[]
d=[]
for i in a:
    if i==" ":
        continue
    else:
        b+=i
for i in b:
    if b.count(i)==1:
        c.append(i)
c=set(c)
d=list(c)
d.sort()
for i in d:
    k+=i
print(k)    

