n=int(input())
a=[]
c=0
for i in range(0,n):
    x=input()
    a.append(x)
for i in a:
    if i=='++X' or i=='X++':
        c+=1
    else:
        c-=1
print(c) 