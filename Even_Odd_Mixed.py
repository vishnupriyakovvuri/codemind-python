n=int(input())
o=0
e=0
while n>0:
    r=n%10
    if r%2==0:
        e+=1
    else:
        o+=1
    n=n//10    
if o>0 and e==0:
    print("Odd")
elif e>0 and o==0:
    print("Even")
else:
    print("Mixed")
    