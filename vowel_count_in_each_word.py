a=input()
b=[]
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
   print(i,end=" ")        