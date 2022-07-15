n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
d=[]
for i in a:
    b.append(a.count(i))
d=set(b)

for i in a:
    if a.count(i)==max(d):
        c.append(i)
c=set(c)
print(min(c))