n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=set(a)
d=set(b)
e=list(c)
f=list(d)
k=[]
c=0
for i in e:
    for j in f:
        if(i==j):
            if i not in k:
                k.append(i)
g=set(e+f)
c=len(k)
print(c)    