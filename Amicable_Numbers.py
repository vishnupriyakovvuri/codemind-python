a=int(input())
b=int(input())
s=0
p=0
for i in range(1,(a//2)+1):
    if(a%i==0):
        s+=i
for i in range(1,(b//2)+1):
    if(b%i==0):
        p+=i
if(p==a and s==b):
    print('Amicable')
else:
    print('Not Amicable')