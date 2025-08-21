# value error,type error, index error,key error, this are runtime error[to handle run time error we use exceptinoal handling]
# if 10%2==0
# print("even") # this type eeor is called 


# exceptional handling
try:
    a=10
    a=a+10
    l=[1,2,3]
    k=l[2]
    d={1:2,2:4,3:9}
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
