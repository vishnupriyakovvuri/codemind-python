def palin(n):
    s=0
    while(n>0):
        r=n%10
        s=s*10+r
        n=n//10
    return s    
    
n=int(input())    
a=list(map(int,input().split()))
b=[]
c=0
for i in range(len(a)):
    print(palin(a[i]),end=" ")