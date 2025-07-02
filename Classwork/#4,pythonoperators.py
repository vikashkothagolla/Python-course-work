a=10
b=20
print("addition(+):",a+b)  
print("substraction(-):",a-b)
print("multiplication(*):",a*b)
print("division(/):",a/b)
print("floor divison(//):",a//b)
print("moduls(%):",a%b)
print("expoential(**):",a**b)

# comparision operator
a=20
b=10
print("equal to(==):",a==b)  # equal to(==):false
print("not equal to(!=):",a!=b)  # not equal to(!=):true
print("greater then(>):",a>b)     # greater then(>):true
print("less then(<):",a<b)           # less then(<):false
print("greater then or equal to(>=):",a>=b)  # reater then or equal to(>=):true
print("less then or eual to(<=):",a<=b)     # less then or eual to(<=):fasle

#Assignment operator
a=10
b=20
print("assign(=):",a) 
print("addition and assign(+=):",a) 
a+=b 
print("substraction and assign(-=):",a)
a-=b
print("multiplication and assign(+*):",a)
a*=b
print("division and assign(/=):",a)
a/=b
print("floor divison and assign(//=):",a)
a//=b
print("moduls and assign(%=):",a)
a%=b
print("expoential and assign(**=):",a)
a**=b

# Logical operators
a=20
b=10
print("And operator:",a>b and b<a)
print("Or operayor:",a>b or a<b)
print("Not operator:",not a>5)

# Membership operator
phone=["samsung","iqoo","mi"]
print("mi" not in phone)
print("iqoo" in phone)

# identity operator
a=[11,12,13,14]
b=a
c=[11,22,33,44]
print(a is  b)
print(b is  a)
print(c is  a)
print(c is not  b)