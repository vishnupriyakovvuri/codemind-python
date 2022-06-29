n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in range(len(a)):
        c.append(a[i]+b[i])    
for i in c:
    print(i,end=" ")
        