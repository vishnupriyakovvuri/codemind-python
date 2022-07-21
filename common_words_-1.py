a=input()
a=a.lower()
b=input()
b=b.lower()
a=a.split(" ")
b=b.split(" ")
c=[]
p=0
for i in a:
    c.append(i)
for i in b:
    c.append(i)
for i in c:
    if c.count(i)!=1:
        p+=1
print(p//2)    