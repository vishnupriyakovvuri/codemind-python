n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
e=list(a)
f=list(b)
k=[]
l=[]
c=0
for i in e:
    r=0
    for j in f:
        if(i==j):
            r+=1
    if(r==0):    
            if i not in k:
                k.append(i)
for i in f:
    r=0
    for j in e:
        if(i==j):
            r+=1
    if(r==0):    
            if i not in k:
                k.append(i)   
for i in k:
    print(i,end=" ")