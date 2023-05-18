N=int(input("enter n:\n"))
for i in range(65,N+65):
    for j in range(65,i+1):
        print(chr(j),end=" ")
    print("\n")    
