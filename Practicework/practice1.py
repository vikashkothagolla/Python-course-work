n=int(input("enter the number: "))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if n==sum:
    print("amstrong no")
else:
    print("not a amstrong no")    















