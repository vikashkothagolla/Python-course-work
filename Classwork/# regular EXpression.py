
'''# it is similar to string but in regular expression we check the patterns
import re
res=re.match(r'[a-z]','hello world')
print(res.group() if res else "No pattern")
'''

'''import re
res=re.match(r'\d{2}','47hello world')
print(res.group() if res else "No pattern")'''

'''
import re
res=re.match(r'[A-Z]','4hello world')
print(res.group() if res else "No pattern")'''


'''# searching for numbers
import re
res=re.match(r'[0-9]{2}','ds-da-78-12')
print(res.group() if res else "No pattern")'''

'''# findall
import re
res=re.findall(r'[0-9]{2}','PES-90 & PFS-80 ds-da-14-15')
print(res)


# finditer[giving postion of no]
import re
res=re.finditer(r'[0-9]{2}','PES-90 & PFS-80 ds-da-14-15')
for i in res:
    print(i.group(),i.start())

# fullmatch[entire pattern should match exactly with same position]
import re
res=re.fullmatch(r'(aeiou)+','aeiou')
print(res.group() if res else "No pattern")

# with *
import re
res=re.fullmatch(r'(aeiou)*','aeiou')
print(res.group() if res else "No pattern")

# with nos
import re
res=re.fullmatch(r'\d{10}','1234567890')
print(res.group() if res else "No pattern")

###
import re
res=re.fullmatch(r'^[6-9]\d{10}','66666666')
print(res.group() if res else "No pattern")

# ... all words
import re
res=re.findall(r'\w','python Pythox')
print(res)

# spaces
import re
res=re.findall(r'\w+','python Pythox java')
print(res)


# 
import re
res=re.split(r'[,;"-]','python,pythox;java')
print(res)

# sub just it replace
import re
res=re.sub(r'[aeiouAEIOU]','*','python programming is good')
print(res)

# numbers are replaced with underscore
import re
res=re.sub(r'[0-9]','_','python9.9 programming is good')
print(res)

# it give the numbers with length only one
import re
res=re.findall(r'\b\d{1}\b','34 78 7 6 5 4 98 6 997990909 8789')
print(res)'''


# full name
name=pattern=r'^[A-Za-z]{2,25} ( [A-Za-z]{2,25})+$'
email=pattern=r'^[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2,3}$'