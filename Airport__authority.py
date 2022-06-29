n=int(input())
a=[]
s=0
for i in range(n):
    a.append(int(input()))
t=int(input())    
for i in a:
    if(i<=t):
        s+=1
    else:
        s+=2
print(s)        
        
    