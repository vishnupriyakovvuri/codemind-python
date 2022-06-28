def prime(n):
    c=0
    if n<=1:
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
c=0
d=0
if(prime(a)==1):
    while(a>0):
      r=a%10
      if prime(r)==1:
        c+=1
      a=a//10
      d+=1
    if(c==d):
        print('Mega Prime')
    else:
        print('Not Mega Prime')
    
else:
    print('Not Mega Prime')