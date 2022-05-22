def fact(i):
    p=1
    while i>=1:
        p=p*i
        i-=1
    return p
t=int(input())
while t!=0:
    n=int(input())
    print(fact(n))
    t-=1
    