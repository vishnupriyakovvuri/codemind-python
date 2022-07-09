n=input()
a=[]
for i in n:
    if(int(i)%2!=0):
        a.append(int(i)*int(i))
s=''
for i in a:
    s+=str(i)
print(s)