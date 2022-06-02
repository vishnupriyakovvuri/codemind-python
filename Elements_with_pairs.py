n=int(input())
a=list(map(int,input().split()))
b=[0]
if len(a)%2==0:
    for i in a:
        print(i,end=" ")
else:
    a.extend(b)
    for i in a:
        print(i,end=" ")