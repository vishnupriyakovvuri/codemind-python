n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
e=list(a)
f=list(b)
k=[]
l=[]
c=0
for i in e:
    for j in f:
        if(i==j):
            if i not in k:
                k.append(i)
for i in f:
    for j in e:
        if(i==j):
            if i not in k:
                k.append(i)   
for i in k:
    print(i,end=" ")