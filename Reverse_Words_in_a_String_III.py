a=input()
c=[]
b=''
d=''
for i in a:
    if(i!=" "):
        b+=i
    else:  
         b=b[-1::-1]    
         c.append(b) 
         b=''
c.append(b[-1::-1])         
for i in range(0,len(c)):
    if i!=len(c)-1:
        d+=c[i]
        d+=" "
    else:
        d+=c[i]
print(d)    
    