def prime(i):
    c=0
    for j in range(2,(i//2)+1):
        if i%j==0:
            c+=1
            break
    if c==0:
        return True
    else:
        return False
n=int(input())
m=int(input())
for i in range(n,m):
    if(i!=1 and prime(i)==1):
        print(i)