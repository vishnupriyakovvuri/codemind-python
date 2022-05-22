def prime(d):
    c=0
    for i in range(2,(d//2)+1):
        if d%i==0:
            c+=1
    if c==0:
        return True
    else:
        return False
n=int(input())
m=int(input())
for i in range(1,100):
    d=n+m+i
    if prime(d)==1:
        print(i)
        break