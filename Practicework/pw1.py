# acute,right,obtuse
a=int(input("enter the angle:"))
if(a==90):
    print("Right Angle")
elif(a>0 and a<=90):
    print("Acute Angle")
elif(a>90 and a<180):
    print("Obtuse Angle")
    
# Input: 22, 25
# Output: Second person is older
n1=int(input("enter the age:"))
n2=int(input("enter the age:"))
if(n2>n1):
    print("Second person is older")
else:
    print("both persons are same age")   

# Input: 36
# Output: Perfect square
num=int(input("enter the num:"))

x = num ** 0.5  # square root

if x == int(x):
    print("Perfect square")
else:
    print("Not a perfect square")

 #Input: 55 Check if a number lies outside the range 10 to 50
# Output: Outside the range   
n=int(input("Enter the number:"))
if n<10 or n>50:
    print("Outside the range")
else:
    print("Inside The range")  

    # Check if temperature is cold (<15°C), moderate (15–30°C), or hot (>30°C)
#Input: 10
#Output: Cold
temp=int(input("Enter the temperature:"))
if temp<15:
    print("Cold")
elif temp>15 and temp<=30:
    print("moderate")
else:
    print("hot")    



