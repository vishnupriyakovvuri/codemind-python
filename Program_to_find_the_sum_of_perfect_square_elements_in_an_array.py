import math
n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    if(i**0.5==int(i**0.5)):
        s+=i
print(s)        
        