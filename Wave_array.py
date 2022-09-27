n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(1,(len(a)-1)):
    if (a[i-1]<a[i] and a[i+1]<a[i] or a[i-1]>a[i] and a[i+1]>a[i]):
        continue
    else:
        c=1
        break
if c==1:
    print('no')
else:
    print('yes')