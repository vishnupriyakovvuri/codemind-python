a=int(input())
b=a*a
p=a
s=0
while(b>0):
    r=b%10
    s+=r
    b=b//10
if(s==p):
    print('Neon Number')
else:
    print('Not Neon Number')
    