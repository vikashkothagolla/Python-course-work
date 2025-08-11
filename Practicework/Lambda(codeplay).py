##########33
'''n=int(input())
oddeven=lambda n:True if n%2==0 else False
print(oddeven(n))'''
#############
'''n=int(input())
square=lambda n:n*n
print(square(n))'''
############
'''a=int(input())
b=int(input())
iseven=lambda a,b:a if a>b else b
print(iseven(a,b))'''
####
'''a=int(input())
b=int(input())
iseven=lambda a,b:a*b
print(iseven(a,b))'''
############
'''l=[(1,7),(8,9),(3,6)]
print(sorted(l,key=lambda x:x[1]))
####### reverse
l=[(1,7),(8,9),(3,6)]
print(sorted(l,key=lambda x:x[1],reverse=True))'''
##### even
'''l=[1,2,3,4,5,6]
e=list(filter(lambda x:x%2==0,l))
print(e)'''
##### list of squares
'''l=[1,2,3,4,5,6]
squares=list(map(lambda x:x*x,l))
print(squares)'''
##### uppercase
'''l=["hello","world"]
e=list(map(lambda x:x.upper(),l))
print(e)'''
# dict soretd
'''data = {'vikas': 35, 'anem': 89, 'sanjay': 100}
sorted_data = dict(sorted(data.items(), key=lambda x: x[1]))
print(sorted_data)'''
# length of the string
'''l="python programming"
le=lambda x:x (l)'''


# check if a string starting with a vowel or not
startwithvowel=lambda string:string[0] in 'aeiou'
print(startwithvowel("vikash"))

#add each no with 10 using map
addten=map(lambda l:l+10,[1,2,3])
print(list(addten))

#  string length >3
stringlong=filter(lambda l:len(l)>3,["vikash","ram","hi"])
print(list(stringlong))

# reduce() product
from functools import reduce
numbers=[1,2,3]
product=reduce(lambda a,b:a*b,numbers)
print(product)

# multiply each no with its index.use map() and enumerate()
numbers=[1,2,3,4]
multiply=list(map(lambda i:i[0]*i[1],enumerate(numbers)))
print(multiply)



# multiple sof 3
multipleof3=filter(lambda i:i%3==0,[1,2,3,4,5,6])
print(list(multipleof3))

#
l=["cat","lion","tiger","god"]
res=len(sorted(l))
print(res)

# sort words a/c to length of word
words = ["apple", "kiwi", "banana", "cherry"]
sorted_words = sorted(words, key=lambda w: len(w))
print(sorted_words)


#lamnda to extract domain
extract_domain = lambda email: email.split('@')[1]
print(extract_domain("user@gmail.com"))  # gmail.com
print(extract_domain("name@yahoo.com"))  # yahoo.com

#get lastdigit
last_digit = lambda num: num % 10
print(last_digit(123))   # 3
print(last_digit(7890))  # 0


# using lambda leap year
is_leap = lambda year: (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(is_leap(2020))  # True
print(is_leap(2025))  # False
