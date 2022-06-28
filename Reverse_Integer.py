a=int(input())
s=0
if a>0:
    while(a>0):
        r=a%10
        s=s*10+r
        a=a//10
    print(s)
else:
    a=abs(a)
    while(a>0):
        r=a%10
        s=s*10+r
        a=a//10
    print(-s)
    
        
        