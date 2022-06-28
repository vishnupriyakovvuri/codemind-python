def prime(n):
    c=0
    if(n<=1):
        c=1
    else:
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                c=1
                break
    if c==0:
        return 1
    else:
        return 0
a=int(input())
b=a
s=0
while(a>0):
    r=a%10
    s=s*10+r
    a=a//10
if prime(b)==1:
    if(prime(s)==1):
        print('circular prime')
    else:
        print('prime but not a circular prime')
else:
    print('not prime')
        