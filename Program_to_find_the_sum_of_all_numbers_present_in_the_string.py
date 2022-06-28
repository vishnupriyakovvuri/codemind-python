a=input()
s=0
for i in a:
    if i in '0123456789':
        s+=int(i)
print(s)        