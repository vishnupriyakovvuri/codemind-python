def palin(n):
    a=n
    s=0
    while(n>0):
        r=n%10
        s=s*10+r
        n=n//10
    if s==a:
        return 1
    else:
        return 0
n=int(input())    
a=list(map(int,input().split()))
b=[]
c=0
for i in range(len(a)):
    if(palin(a[i])==1):
        c+=1
print(c)