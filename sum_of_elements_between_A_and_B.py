n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
k=0
for i in a:
        if(i>=b and i<=c):
            k=k+i
print(k)