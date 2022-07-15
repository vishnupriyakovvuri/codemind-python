n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in a:
    if i==0:
        b.append(i)
    else:
        c.append(i)
b.extend(c)
for i in b:
    print(i,end=" ")