a=input()
c=0
for i in a:
    if i in '!@#$%^&*()_,[]{}|?.':
        c+=1
print(c)