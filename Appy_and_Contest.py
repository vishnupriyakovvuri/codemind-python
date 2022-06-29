def gcd(a,b):
    if(a<b):
        c=a
    else:
        c=b
    for i in range(c,0,-1):
        if(a%i==0 and b%i==0):
            return i
            break
def lcm(a,b):
    if(gcd(a,b)==1):
        return a*b
    else:
      if(a>b):
        c=a
      else:
        c=b
      while(1):
        if(c%a==0 and c%b==0):
            return c
            break
        c+=1
t=int(input())
while t>0:
    a,b,c,d=map(int,input().split())
    e=a//b
    f=a//c
    g=a//lcm(b,c)
    h=e+f-g
    if(h>d):
        print('Win')
    else:
        print('Lose')
    t-=1