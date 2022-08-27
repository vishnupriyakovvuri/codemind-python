n=int(input())
l=list(map(int,input().split()))
k=int(input())
r=k%len(l)
s=len(l)-r
p=[]
if(k>0):
    for i in range(s,len(l)):
       p.append(l[i])
    for i in range(0,s):
        p.append(l[i])
    for i in p:
        print(i,end=" ")
else:
    for i in range(0,s):
        p.append(l[i])
    for i in range(s,len(l)):
       p.append(l[i])
    for i in p:
        print(i,end=" ")