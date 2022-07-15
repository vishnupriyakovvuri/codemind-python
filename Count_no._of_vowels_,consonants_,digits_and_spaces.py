a=input()
v=0
c=0
w=0
d=0
for i in a:
    if i in 'aeiouAEIOU':
        v+=1
    elif i in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
        c+=1
    elif i in'1234567890':
        d+=1
    elif i==" ":
        w+=1
print('Vowels:',v) 
print('Consonants:',c)
print('Digits:',d)
print('White spaces:',w)