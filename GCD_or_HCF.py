n,m=map(int,input().split())
if n>m:
    a=m
else:
    a=n
for i in range(a,0,-1):
    if(n%i==0 and m%i==0):
        print(i)
        break