n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
d=[]
e=0
for i in a:
        if(i>=b and i<=c):
            d.append(i)
k=100            
for i in a:
        if i not in d:
            if (i<k):
                e+=1
                k=i
if(e>0):                
    print(k)
else:
    print(-1)