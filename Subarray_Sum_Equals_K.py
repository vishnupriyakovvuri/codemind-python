n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(n):
    s=l[i]
    if s==k:
        c+=1
    for j in range(i,n):
        if i==j:
            continue
        else:
            s+=l[j]
            if s==k:
                c+=1
                break
print(c)            