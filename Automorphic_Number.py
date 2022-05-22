a=int(input())
b=a*a
c=0
d=0
while a>0:
    r=a%10
    p=b%10
    if(r==p):
        c+=1
    d+=1    
    a=a//10
    b=b//10
if c==d:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')
    
