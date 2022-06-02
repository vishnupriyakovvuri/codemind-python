n=int(input())
a=list(map(int,input().split()))
k=int(input())
b=[]
c=0
for i in a:
    if(k==a.count(i)):
        if i not in b:
            b.append(i)
            c+=1
if c>0:
    for i in b:
        print(i,end=" ")
else:
    print('-1')
