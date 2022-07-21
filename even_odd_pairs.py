n=int(input())
o=[]
e=[]
p=[]
a=list(map(int,input().split()))
for i in a:
    if(i%2==0):
        e.append(i)
    else:
        o.append(i)
if(len(e)<=len(o)):
    for i in range(len(e)):
        p.append(e[i])
        p.append(o[i])
    for i in range(len(e),len(o)):
        p.append(o[i])
else:
    for i in range(len(o)):
        p.append(e[i])
        p.append(o[i])
    for i in range(len(o),len(e)):
        p.append(e[i])
if len(p)%2!=0:
    p.append(0)
for i in p:
    print(i,end=" ")