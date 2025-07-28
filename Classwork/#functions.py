''' 
def function_name(fname):
    print(fname + " hello babu")
function_name("heloo")
function_name("jai")    
         
def my_function():
    print("vikash yadav")
my_function()    

def my_function(fname,lname):
    print(fname + " "  + lname)
my_function("hello","vikash")

def my_function(*kids):
    print("the youngest kid is",kids[2])
my_function("varun","arun","dhawan")   


def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
  '''
'''
# positional Arguments
data=('abc@gmail.com','abc123')
def my_functionb(username,mail,password):
    if mail==data[0] and password==data[1]:
        print(f"{username}-login succeful")
    else:
        print(f"{username}-invalid")
username=input("Enter the user name: ")
mail=input("Enter the mail: ")
password=(input("Enter the password: "))     
my_functionb(username,mail,password)
'''
''' ## key  value arguments my_functionb(mail=mail,password=password,username=username,)
data=('abc@gmail.com','abc123')
def my_functionb(username,mail,password):
    if mail==data[0] and password==data[1]:
        print(f"{username}-login succeful")
    else:
        print(f"{username}-invalid")
username=input("Enter the user name: ")
mail=input("Enter the mail: ")
password=(input("Enter the password: "))     
my_functionb(mail=mail,password=password,username=username,)
'''

'''## default parameters
data=('abc@gmail.com','abc123')
def my_functionb(mail,password,username="vikash"):
    if mail==data[0] and password==data[1]:
        print(f"{username}-login succeful")
    else:
        print(f"{username}-invalid")
username=input("Enter the user name: ")
mail=input("Enter the mail: ")
password=(input("Enter the password: "))     
my_functionb(mail,password) '''

'''#variable length arguments. one * for single sum
def sum(*l):
  s=0
  for i in l:
    s=s+i
  return s
 
print(sum(1,2,3,4,5))
print(sum(1,23,2))
print(sum(1,5,6))
#variable length arguments. two ** for student and marks
def display(**l):
    return l
print(display(p=1,o=2,i=3))
print(display(a=1,b=23))
print(display(v=1))
 '''
def my_function():
    msg="hello world"
    print(msg)
my_function()    

