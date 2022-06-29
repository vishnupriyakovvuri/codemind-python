t=int(input())
while(t>0):
    n=int(input())
    b=list(map(int,input().split()))
    a=[]
    for i in range(1,n+1):
        a.append(i)
    c=a+b
    for i in c:
        if(c.count(i)==1):
            print(i)
            break
        
        
        