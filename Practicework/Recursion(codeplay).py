# 1 to n
'''def oneton(n):
    for i in range(1,n+1):
        print(i,end=" ")
oneton(6) 
'''

# n to 1
'''def oneton(n):
    for i in range(n,0,-1):
        print(i,end=" ")
oneton(6)'''

# first n no's sum
'''def nsum(n):
    sum=0
    for i in range(n+1):
        sum+=i
    return sum
print(nsum(5))'''

#factorial
'''def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))'''

# string
'''l="vikash"
print(l[::-1])'''
# fib
'''def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(6))'''

#sumof digits
'''def sum_of_digits(n):
    if n < 10:
        return n
    else:
        total = 0
        while n > 0:
            digit = n % 10
            total = total + digit
            n = n // 10
        return sum_of_digits(total)

print(sum_of_digits(123))'''
# count nos
def countno(n):
    count = 0
    if n == 0:
        return 1
    while n > 0:
        count = count + 1
        n = n // 10
    return count    

print(countno(123))  # Output: 3

# power
'''def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
print(power(2, 3))  # outpiut:8'''

'''#gcd
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(6,12))'''
# max of 3 no's
'''def max_find(list):
    max_num=list[0]
    for num in list:
        if num>max_num:
            max_num=num
    return max_num    
print(max_find([1,6,4,5,7]))'''

# check if a list is palindrome or  not
def list(l):
 if l==l[::-1]:
    print("True")
 else:
    print("False")  
list([1,2,3,4])
list([1,2,2,1])

# 14
def sum_list(lst):
    # Base case: if list is empty, sum is 0
    if not lst:
        return 0
    # Recursive case: first element + sum of the rest
    return lst[0] + sum_list(lst[1:])

numbers = [1, 2, 3]
print(sum_list(numbers))  # 6

# 15 count occurrences of no's in a list
def occ(list,x):
   if not list:
      return 0
   if list[0]==x:
      return 1+occ(list[1:],x)
   else:
      return occ(list[1:],x)
print(occ([1,2,3,1,3,3],3))

# permutation of a string


# replace char
def replace_char(s, old, new):
    if not s:
        return ""
    first = new if s[0] == old else s[0]
    return first + replace_char(s[1:], old, new)

# Test cases
print(replace_char("abab", 'a', 'x'))  # xbxb
print(replace_char("hello", 'l', 'z')) # hezzo


# binary number
def to_binary(n):
    if n == 0:
        return ""
    return to_binary(n // 2) + str(n % 2)

# Test cases
print(to_binary(5) or "0")  # "101"
print(to_binary(8) or "0")  # "1000"

# palindrome
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

# Test cases
print(is_palindrome("madam")) # True
print(is_palindrome("hello")) # False

#  Find first index of element in list
def first_index(lst, x, idx=0):
    if idx == len(lst):
        return -1
    if lst[idx] == x:
        return idx
    return first_index(lst, x, idx + 1)

# Test cases
print(first_index([1, 2, 3, 2, 5], 2))  # 1
print(first_index([4, 5, 6], 1))        # -1


