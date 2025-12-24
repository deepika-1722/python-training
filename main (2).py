x=int(input())
for i in range(1,x+1):
        print("*"*i)



second method
x=int(input())
for i in range(x):
    for j in range(i+1):
        print("*",end=" ")
    print()
    
