a=int(input())
b=a
s=0
while a>0:
    r=a%10
    s=s*10+r
    a=a//10
if(s==b):
    print('True')
else:
    print('False')