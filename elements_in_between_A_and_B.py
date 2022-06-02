n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
d=[]
e=0
for i in a:
        if(i>=b and i<=c):
            d.append(i)
            e+=1
if e>0:
    for i in d:
        print(i,end=" ")
else:
    print('-1')