n=int(input())
a=list(map(int,input().split()))
c=[]
k=0
for i in range(len(a)):
    if a[i]!=0:
        c.append(a[i])
        k+=1 
d=len(a)-k        
while(d!=0):
    c.append(0)
    d-=1
for i in c:
    print(i,end=" ")
    
        