# value error,type error, index error,key error, this are runtime error[to handle run time error we use exceptinoal handling]
# if 10%2==0
# print("even") # this type eeor is called 


# exceptional handling
'''try:
    a=10
    a=a+10
    l=[1,2,3]
    k=l[2]
    d={1:2,2:4,3:9}
    b=int(input("Enter a number: "))
    print(b)
    c=1+"1"
except NameError:
    print("a is not defind")
except IndexError:
    print("you havr entered the out of range value")
except KeyError:
    print("key is not present")
except TypeError:
    print("no two data types are added")        
# or instead all 4 types of erros in above,we can write in single line as below
except(NameError,IndexError,KeyError,ValueError,TypeError) as e:
    print(f"Error occured: {e}")'''

try:
    a=10
    a=a+10
    l=[1,2,3]
    k=l[2]
    d={1:2,2:4,3:9}
    b=int(input("Enter a number: "))
    print(b)
    c=1+12
except Exception as e:
    print(f"Error occured: {e}")
else:
    print("No errors")
    print(c)
finally:
    print("---------code executed--------------")

