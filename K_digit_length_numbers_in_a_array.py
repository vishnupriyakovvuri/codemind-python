n,k=map(int,input().split())
a=list(map(int,input().split()))
d=[]
c=0
for i in a:
    i=abs(i)
    d.append(len(str(i)))
for i in range(0,len(d)):
    if d[i]==k:
        c+=1
print(c)     