s=input()
a=s.split(" ")
e=[]
o=[]
t='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'
for i in a:
    e.append(i[: :-1])
for i in range(len(e)-1,-1,-1):
    o.append(e[i])
t+=" ".join(o)
print(t)    
        