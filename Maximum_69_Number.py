import math
a=int(input())
d=int(math.log(a,10))
f=0
r=1
while a>0:
 if r!=0 :   
    r=a//pow(10,d)
    if(r==6 and f==0):
        print(9,end="")
        f=1
    else:
        print(r,end="")
 a=int(a%pow(10,d))
 d-=1
        