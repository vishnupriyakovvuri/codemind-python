n=int(input())
a=list(map(int,input().split()))
b=[0]
c=1
if len(a)%2==0:
    for i in range(len(a)//2):
        print(a[i],a[len(a)-c],end=" ")
        c+=1
else:
    for i in range(len(a)//2+1):
        if(i<len(a)-c):
            print(a[i],a[len(a)-c],end=" ")
        c+=1
    print(a[len(a)//2],'0',end=" ")