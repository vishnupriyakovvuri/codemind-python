from itertools import permutations
a=input()
b=list(a)
c=permutations(a)
for i in c:
    d=''
    for j in i:
        d+=j
    print(d)    
    
    