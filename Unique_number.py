a=int(input())
b=[]
c=0
while a>0:
    r=a%10
    b.append(r)
    a=a//10
for i in b:
    if(b.count(i)>1):
        c=1
        break
if(c==0):
    print('Unique Number')
else:
    print('Not Unique Number')

    
    