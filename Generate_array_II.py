n=int(input())
a=list(map(int,input().split()))
r=[]
q=[]
c=[]
for i in range(0,len(a),2):
    q.append(a[i])
for i in range(1,len(a),2):
    r.append(a[i])
for i in range(0,len(q)):
    for j in range(0,r[i]):
        c.append(q[i])
print(*c)        
    