n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(len(a)):
    p=1
    for j in range(len(a)):
        if(i==j):
            continue
        else:
            p=p*a[j]
    b.append(p)    
for i in b:
    print(i,end=" ")
        
        