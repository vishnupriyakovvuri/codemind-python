n=int(input())
a=list(map(int,input().split()))
b=list(set(a))
for i in b:
    print(i,end=" ")