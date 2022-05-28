n=int(input())
if n<3:
    print('The pattern is not possible')
else:    
    for i in range(1,n+1):
       for j in range(1,i+1):
          print("*",end="")
       print() 
    i=n+1   
    for i in range(1,n):
        for j in range(1,n-i+1):
            print('*',end="")
        print()    
       