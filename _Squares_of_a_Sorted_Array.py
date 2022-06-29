n=int(input())
a=list(map(int,input().split()))
c=[]
for i in range(len(a)):
    if a[i]<0:
        a[i]=abs(a[i])
b=list(sorted(a))
for i in b:
    c.append(i*i)
for i in c:
    print(i,end=" ")
    