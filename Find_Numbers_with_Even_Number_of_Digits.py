def digit(n):
    c=0
    if n==0:
        c=1
    if n<0:
        n=abs(n)
    while(n>0):
        r=n%10
        c+=1
        n=n//10
    return c
n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(len(a)):
   if digit(a[i])%2==0:
       c+=1
print(c)          