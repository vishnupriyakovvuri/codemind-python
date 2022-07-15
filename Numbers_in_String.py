a=input()
c=0
for i in a:
    if i in '0123456789':
        c+=int(i)
print(c)        