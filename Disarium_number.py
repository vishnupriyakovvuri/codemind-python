import math
a=int(input())
n=a
s=0
d=int(math.log(a,10))
d=d+1
while a>0:
    r=a%10
    s=s+pow(r,d)
    a=a//10
    d-=1
if(n==s):
    print('True')
else:
    print('False')
