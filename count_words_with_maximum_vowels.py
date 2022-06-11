a=input()
b=[]
min=0
m=0
k=0
for i in a:
    if i==' ':
       b.append(k)
       k=0
    else:
          if i in'AEIOUaeiou':
              k+=1
b.append(k)
for i in b:
    if i>min:
        min=i
for i in b:
    if i==min:
        m+=1
print(m)        