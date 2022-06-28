a=int(input())
b=[]
while(a>0):
    r=a%10
    b.append(r)
    a=a//10
print(max(b))    
