'''# reverse string using "vikash"
def rev(string):
    if len(string)<=1:
        return string
    else:
        return rev(string[1:])+string[0]
print(rev("vikash"))'''


'''first n natural numbers
def first_n_naturalnos(n):
    sum=0
    for i in range(1,n+1):
         sum+=i
    return sum
print(first_n_naturalnos(5))'''

'''# factorial
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
       return n*factorial(n-1)
    return factorial
print(factorial(100))'''

'''# update values in dict
def update(n):
   for value in n:
     n[value]=n[value]+1
   return n
print(update({'a':1,'b':2}))'''   


'''# clear
l=[1,2,3,4]
res=l
res=l.clear()
print(res)
'''
#  123=>246 in list
def double(list):
    return [i*2 for i in list]
print(double([1,2,3]))

# append 123 to add 1234
def add(list):
 res=list.append(4)
 print(list)
add([1,2,3])

# len of string
def length(n):
 return len(n)
print(length("vikash"))

#ptr
def ptr(P,T,R):
  return (P*T*R)/100
print(ptr(1000,2,5))

#mutliply of 3 nos
def ptr(P,T,R):
  return (P*T*R)
print(ptr(1000,2,5))

'''# greet the user
n=input("enter the name: ")
name="Hello"
res=print(name+"  "+ n)
res'''

# sorted list
l=[1,2,3,41,2,0,-1,-3,]
res=sorted(l)
print(res)
# or
def sort(list):
  return sorted(list)
print(sort([1,2,3,41,2,0,-1,-3,]))

# clear list
def cle(list):
  list.clear()
cle([1,2,3,4,5])


'''# Take dictionary input (eval is used here for simplicity, but in real apps use safer methods)
d = eval(input("Enter dictionary: "))
key = input("Enter key to update: ")
new_value = input("Enter new value: ")
# If the value is a number, convert it
if new_value.isdigit():
    new_value = int(new_value)
d[key] = new_value
print("Updated dictionary:", d)
'''

# power a^b
def power(a,b):
  return a**b
print(power(2,3))

# 1234 == 10
def sumofdigit(n):
  sum=0
  for i in str(n):
    sum+=int(i)
  return sum
print(sumofdigit(12345))

# madam==true palideome
def str(n):
  if len(n)==len(n[::-1]):
    return True
print(str("MADAM"))  

# gcd using math build in functions
import math

a, b = map(int, input("Enter two numbers: ").split())
print("GCD is:", math.gcd(a, b))

# gcs using recursion
def gcd(a, b):
    # Base case: if b is 0, GCD is a
    if b == 0:
        return a
    # Recursive case: call gcd with (b, remainder of a/b)
    return gcd(b, a % b)

# Taking input from user
a, b = map(int, input("Enter two numbers: ").split())

# Display result
print("GCD is:", gcd(a, b))
