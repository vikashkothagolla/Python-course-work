#if and else
items=['car','bike','scooty']
print("welcome to flipcart".center(80,'-'))
searchitem=input("enter the item: ").lower()

if searchitem in items:
    print("found ")
else:
    print("not found")    

# if ,elif and else
amo=int(input('enter amount'))
if amo>50000:
    print("go to goa")
elif amo>25000:
    print("go to shopping")
elif amo>15000:
    print("got to maintaince")
else:
    print("save amount")               

# if and else

name=input("enter the name:")
vowels='aeiouAEIOU'

if name[0] in vowels:
    print("+ve")
else:
    print("-ve")    


    # +ve and -ve no
a=int(input("enter the number:"))
if(a>0):
    print("+ve no")
elif(a<0):
    print("-ve no")
else:
    print("zero")  

 # even or odd
a=int(input("enter the number:"))
if(a%2==0):
    print("even")
else:
    print("odd")    
 # leap no

year=int(input('enter the year: '))
if year%400==0 or year%4==0 and year%100!=0:
    print("f{year} it is a leap year")
else:
      print("f{year} it is a not leap year")        

