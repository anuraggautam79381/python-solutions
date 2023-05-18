def fact(n):
    if n<=1:
        return 1
    else:
        n=n*fact(n-1)
    return n

n=int(input("enter number:\n"))
print("factorial of",n,"is:\n",fact(n))            
