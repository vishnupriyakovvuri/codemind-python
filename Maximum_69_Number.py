n=int(input())
p=n
d=-1
flag=0
while n>0:
    d+=1
    n=n//10
while p>0:
    r=p//int(pow(10,d))
    if r==6 and flag==0:
        print("9",end="")
        flag=1
    else:
        print(r,end="")
    p=p%int(pow(10,d))
    d-=1