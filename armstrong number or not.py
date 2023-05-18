n=int(input("enter the number:\n"))
x=len(str(n))
c=n
sum=0
while(n>0):
    r=n%10
    sum=sum+r**x
    n=n//10
if(c==sum):
    print("armstrong number")
else:
    print("not armstrong")
