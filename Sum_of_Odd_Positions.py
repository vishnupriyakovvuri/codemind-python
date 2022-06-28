n=int(input())
a=list(map(int,input().split()))
e=0
for i in range(0,len(a)):
    if(i%2!=0):
        e+=a[i]
print(e)   