def digit(n):
    c=0
    if n<0:
        n=abs(n)
    while(n>0):
        r=n%10
        c+=r
        n=n//10
    return c
n=int(input())    
a=list(map(int,input().split()))
c=0
for i in range(len(a)):
    c+=digit(a[i])
print(c)    