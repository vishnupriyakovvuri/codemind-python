def rev(n):
    s=0
    while(n>0):
        r=n%10
        s=s*10+r
        n=n//10
    return s    
a=int(input())
b=a*a
c=rev(b)
e=int(c**0.5)
f=rev(e)
if (a==f):
    print('True')
else:
    print('False')

