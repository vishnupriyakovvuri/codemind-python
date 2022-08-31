n=int(input())
b=list(map(int,input().split()))
m=int(input())
e=list(map(int,input().split()))
q=int(input())
c=0
for i in range(0,n):
    for j in range(b[i],(e[i]+1)):
        if j ==q:
            c+=1
print(c)  