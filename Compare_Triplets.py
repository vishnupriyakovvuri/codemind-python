a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=0
c=0
for i in range(3):
    if(a[i]>b[i]):
        s+=1
    elif(a[i]<b[i]):
        c+=1
print(s,c)
        