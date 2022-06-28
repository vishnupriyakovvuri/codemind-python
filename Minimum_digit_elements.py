def digit(n):
    c=0
    while n>0:
        r=n%10
        c+=1
        n=n//10
    return c
n=int(input())    
a=list(map(int,input().split()))
b=[]
for i in range(len(a)):
    b.append(digit(a[i]))
print(b.count(min(b)))