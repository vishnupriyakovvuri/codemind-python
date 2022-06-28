a=int(input())
if(a==1 or a==7):
    print('True')
else:
    while(a>=10):
        s=0
        while(a>0):
            r=a%10
            s=s+r*r
            a=a//10
        a=s
    if(a==1 or a==7):
        print('True')
    else:
        print('False')
            
