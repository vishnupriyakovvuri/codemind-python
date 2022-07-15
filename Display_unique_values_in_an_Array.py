n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in a:
    if(a.count(i)==1):
        b.append(i)
        c+=1
if c>0:
    for i in b:
        print(i,end=" ")
else:
    print('-1')