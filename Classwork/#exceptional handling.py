''' # a=a+10 it gives output as nameError
#  then how to hadle it,by just using try[it check whether my code has any errors or not,if it throws any errors it gives to the except block] and except
try:
    a=a+10
except NameError:
    print("a is not defind")


# indexError
try:
    a=10
    a=a+10
    l=[1,2,3]
    k=l[7] # it shows indexerror[to over come this error we use the another except block]
except NameError:
    print("a is not defind")
except IndexError:
    print("you have entered the out of range value")

# keyError
try:
    a=10
    a=a+10
    l=[1,2,3]
    k=l[2]
    d={1:1,2:4,3:9} # it is an akeyerror
    print(d[9]) # it dict doenot have any key value as 7 to hadle it we use other except
except NameError:
    print("a is not defind")
except IndexError:
    print("you have entered the out of range value")
except KeyError:
    print("7 key is not present ")


# Value Error
try:
    a=10
    a=a+10
    l=[1,2,3]
    k=l[2]
    
    n=int(input("enter the number:")) # valueerror[if we give no no pbm else we give any string it shows as valueError, to handle it we use except block ]
    print(n) 
except NameError:
    print("a is not defind")
except IndexError:
    print("you have entered the out of range value")
except KeyError:
    print("7 key is not present ")
except ValueError:
    print(" enter the proper data")


# Type error
try:
    a=10
    a=a+10
    l=[1,2,3]
    k=l[2]
    n=int(input("enter the number:")) 
    print(n)
    c=1+"1" # TypeError
except NameError:
    print("a is not defind")
except IndexError:
    print("you have entered the out of range value")
except KeyError:
    print("7 key is not present ")
except ValueError:
    print(" enter the proper data")
except TypeError:
    print("you can't add 2 differnt numbers")


        # or below on can perform all above Errors
try:
   a=a+10
   l=[1,2,3]
   k=l[2]
   d={1:2,2:4,3:9}
   print(d[2])
   b=int(input("enter the number: "))
   print(b)
   c=1+12
except (NameError,IndexError,KeyError,ValueError,TypeError) as e:
    print(f"Error occured:{e}")  
   
    
# or below on can perform all above Errors

try:
  
   l=[1,2,3]
   k=l[2]
   d={1:2,2:4,3:9}
   print(d[2])
   b=int(input("enter the number: "))
   print(b)
   c=1+12
except Exception as e:
    print(f"Error occured:{e}") 
else:
    print("NO Errors")
    print(c)
finally:
    print("code excecuted") '''


# 
try:
    amount=int(input("enter the amount: "))
    if amount<0:
        raise ValueError("Enter the positive value")
except Exception as e:
    print(f"Error occured:{e}")
else:
    print("No Errors")
    print("You can withdraw")
finally:
    print("----------Remove your card----------")    


