n=int(input())
a=list(map(int,input().split()))
c=[]
for i in range(len(a)):
    if a.count(a[i])>1:
        if a[i] not in c:
            c.append(a[i])    
for i in c:
    print(i,end=" ")
        