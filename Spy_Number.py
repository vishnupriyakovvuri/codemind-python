a=int(input())
s=0
p=1
while(a>0):
    r=a%10
    s+=r
    p*=r
    a=a//10
if(s==p):
    print('Spy Number')
else:
    print('Not Spy Number')
    
