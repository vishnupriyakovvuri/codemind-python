a=input()
b=[]
k=[]
c=''
d=''
for i in a:
    if i!=" ":
        c+=i
    else:
        b.append(c)
        c=''
b.append(c)
for i in range(len(b)-1,-1,-1):
    k.append(b[i])
for i in range(0,(len(k)-1)):
    d+=k[i]
    d+=" "
d+=k[len(k)-1]   
print(d)    
    
