n=int(input())
if n%2==0:
    t=n//2
else:
    t=(1+n)//2
    
for i in range(1,n+1):
    for j  in range(1,n-1):
        #if(j<=t):
        print(j,end="")
        #else:
        #    if(j-t!=t):
          #      print(j-t,end="")
    for j in range(1,n-2):
        print(j,end="")
        
    print("")