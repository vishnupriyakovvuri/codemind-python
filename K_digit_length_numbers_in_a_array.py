def digit(n):
    c=0
    if(n<0):
        n=abs(n)
    if(n==0):
        c=1
    while n>0:
        r=n%10
        c+=1
        n=n//10
    return c
n,k=map(int,input().split())    
a=list(map(int,input().split()))
b=[]
s=0
for i in range(len(a)):
    b.append(digit(a[i]))
for i in range(len(b)):
    if(b[i]==k):
        s+=1
print(s)        
        