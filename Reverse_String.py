a=input()
b=a.split(" ")
s=b[-1::-1]
p=''
for i in range(len(s)):
    p+=s[i]
    if(i<len(s)-1):
        p+=" "
print(p)    