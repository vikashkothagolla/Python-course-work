'''# eul and iso triangle
a=int(input("enter no: "))
b=int(input("enter no:"))
c=int(input("enter no: "))
if a==b and b==c:
    print("Equilateral")
else:
    print("Isosceles")'''   

# vowel,consonant,digit,special char
ch=input("Enter the ch:")
vowels="aeiouAEIOU"
if ch.isalpha():
 if ch in vowels:
    print("it is vowel")
 else:
    print("consonants")
elif ch.isdigit():
   print("Digit")
else:
   print("Special character")            
# electricity bill
units=int(input("enter the no:"))
if units<=100:
   bill=units*1
elif units<=200:
   bill=(100*1)+(units-100)*2
else:
   bill=(100*1)+(100*2)+(units-200)*3
print(bill)   
# Amstrong no
n=int(input("enter the no"))
sum=0
temp=n
while temp>0:
   digit=temp%10
   sum=sum+digit**3
   temp//=10
if sum==n:
 print("amstron")
else:
   print("not amstrong")
# valide phone no
n=int(input("enter the no: "))
if len(n)==10 and n[0] in '6789' and n.isdigit():
   print("Valid")
else:
   print("invalid")

# improving or declining
n1=int(input("enter the no:" ))
n2=int(input("enter the no:" ))
n3=int(input("enter the no:" ))
if n1>n2>n3:
   print("improving")
else:
   print("declining") 

# duplicate digit => input as 121 and output as duplicate
num=int(input("enetr 3 digit"))
if num[0]==num[1] or num[1]==num[2] or num[0]==num[2]:
   print("duplicates")
else:
   print("unique digits")



