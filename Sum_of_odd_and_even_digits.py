n=int(input())
a=list(map(int,input().split()))
b=[]
e=0
o=0
for i in range(len(a)):
    if(i%2==0):
        e+=a[i]
    else:
        o+=a[i]
d=abs(e-o)
if(d==0):
    print('YES')
else:
    print('NO')
    