a=input()
a=a.lower()
b=''
c=[]
for i in a:
    if i==" ":
        continue
    else:
        b+=i
for i in b:
    if b.count(i)==1:
        c.append(i)
c=set(c)
print(len(c))
    