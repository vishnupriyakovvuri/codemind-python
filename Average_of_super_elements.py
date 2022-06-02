n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
k=0
for i in a:
    if(i==a.count(i)):
        if i not in b:
            b.append(i)
            c+=1
for i in b:
    k=k+i
if c>0:    
   d=k/c
   print("%.2f"%d)
else:
    print('-1')
