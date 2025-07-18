n=int(input("enter the size:"))
for i in range(n):
    for j in range(i+1):
        print('*',end=" ")
    print()    

for i in range(5):
    for j in range(i+1):
        print(i,end=" ")
    print()    

for i in range(5):
    for j in range(5):
        print('*',end=" ")
    print()    

n=int(input("enter the size:"))
for row in range(n):
    for col in range(row-1):
        print('*',end=" ")
    print()    

n=int(input("enter the size:"))
for row in range(n):
    for col in range(n-row-1):
        print('*',end=" ")
    for col in range(row+1):    
     print()    
