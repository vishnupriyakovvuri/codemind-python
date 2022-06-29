n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    c=0
    for j in a:
        if(j<i):
            c+=1
    b.append(c)
for i in b:
    print(i,end=" ")