n=int(input())
a=list(map(int,input().split()))
c=0
s=0
for i in range(0,len(a)):
    if(i<n//2):
        c+=a[i]
    else:
        s+=a[i]
e=abs(c-s)
if(e%4==0):
    print('X')
else:
    print('Y')

    