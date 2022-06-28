def prime(n):
    c=0
    if(n<=1):
        c=1
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            c+=1
    if c==0:
        return 1
    else:
        return 0
n=int(input())
c=0
d=0
a=list(map(int,input().split()))
for i in a:
    if(prime(i)==1):
        d+=1
        c+=i
e=c/d        
print("%.2f"%e)