a=input()
b=[]
min=100
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
    if i<min:
        min=i
print(min)        