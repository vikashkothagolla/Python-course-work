
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

#bitwise operator
a=2
b=4
print("and operator:",a&b)
print("or operator:",a|b)            
print("XOR operator:",a^b)
print("Not operator:",~b)
print("left shift operator:",a<<b)
print("right shift operator:",a>>b)

# operations of strings
n1="vikash"
n2="yadav"
print("concatenation of strings:",n1+n2)
print("vikash" *3)
print(n1[4])
print(n2[2])
print(n1[0:4])
print(n2[:2])
print('vikash' in n1)
print("python" not in n2)

#built in string functions
k="python programming"
print(len(k))
print(max('Vikash'))
print(min("Vikash"))
print(sorted('python'))
print(chr(97))
print(ord('s'))

#python string methods 
# case conversion methods
x="health is wealtth"
print(x.upper())
print(x.lower())
print(x.capitalize())
print(x.title())
y='PyThOn'
print(y.swapcase())


# Alignment and formatting method
y='tit for tat'
print(y.center(30,"*"))
print(y.center(20,"_"))
print(y.rjust(20,'_'))
print(y.ljust(20,"_"))
w="899"
print(w.zfill(5))


#search and find methods
u="varunsanjaytharun"
print(u.find("sanjay"))
print(u.find('s'))
print(u.count('a'))
print(u.index('v'))
print(u.rfind("a"))


# String Testing Methods 
a="pyhton"
print(a.startswith("ki"))
print(a.endswith("on"))
print(a.isalpha())
b="vikash123"
print(b.isalnum())
print(a.islower())
print(a.islower())
print(" ".isspace())

#5. Replace & Modify Methods
text1="sanjay"
print(text1.replace("j","a"))
print(text1.translate(str.maketrans("a","k")))
print(text1.maketrans("hi","ya"))

#6. Splitting & Joining Methods
print(text1.split(" "))#Splits the string into a list by sep
print(text1.rsplit(" "))# Splits from the right side.
print(text1.splitlines(" "))#Splits at line breaks ( ).
result=' '.join(text1)# Joins elements with a separator.
print(result)
text2="hello-ravi"#Splits into a 3-part tuple at first sep.
print(text2.partition("-"))
print(text2.rpartition("-"))# Splits into a3-part tuple at last sep.

#7. Whitespace & Trimming Methods
print("  ram ".strip()) #Removes leading and trailing characters (default: spaces).
print("---ram".lstrip("-"))#Removes leading characters.
print("ram---".rstrip("-")) #Removes trailing characters.
