n=int(input())
a=list(map(int,input().split()))
d=[]
e=[]
for i in a:
    d.append(len(str(i)))
for i in range(0,len(d)):
    if d[i]==max(d):
        e.append(a[i])
print(*e)        
        