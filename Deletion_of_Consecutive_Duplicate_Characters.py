t=int(input())
for i in range(1,t+1):
    a=input()
    b=[]
    c=0
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            c+=1
    print(c)        
    