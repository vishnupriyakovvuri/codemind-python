def palin( i):
    k=i
    rev=0
    while i>0:
        r=i%10
        rev=rev*10+r
        i=i//10
    if rev==k:
        return 1
    else:
        return 0
n=int(input())
m=int(input())
for i in range(n,m+1):
    if(palin(i)==1):
        print(i,end=" ")