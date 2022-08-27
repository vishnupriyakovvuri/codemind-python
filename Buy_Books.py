n=int(input())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
r=0
s=0
for i in range(0,n):
    r+=l[i]
    s+=k[i]
p=s-r
if(p>0):
    print(p)
else:
    print('0')
    