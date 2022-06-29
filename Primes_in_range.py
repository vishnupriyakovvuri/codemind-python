def prime(n):
    if(n<2):
        return(False)
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return(False)
    else:
        return(True)
n=int(input())
m=int(input())
dc=0
for i in range(n,m+1):
    if prime(i):
        dc+=1
print(dc)        