def selfd(p):
    c=0
    s=0
    t=p
    if p<10:
        return 1
    else:
        while(p>0):
            r=p%10
            if r>0:
             if(t%r==0):
                s+=1
            p=p//10
            c+=1
    if(c==s):
        return 1
    else:
        return 0
n=int(input())
m=int(input())
for i in range(n,m+1):
    if(selfd(i)==1):
        print(i,end=" ")
        