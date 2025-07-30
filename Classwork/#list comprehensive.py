# print numbers from a given range
'''n=int(input("enter the number: "))
l=[]
for i in range(1,n+1):
     if i%2==0:
         l.append(i)
print(l)

s=[i for i in range(1,n+1) if i%2==0]
k=[i for i in range(1,6)]
print(s,k)
'''
# square
''''d=[]
for i in range(5):
     d.append(i*i)
print(d)

d=[i*i for i in range(5)]     
'''
# upper case of python
'''
s='python'
for i in s:
    s.append(s.upper())
print(s)
'''
'''s=[i.upper() for i in s]
j='python'
vol="aeiouAEIOU"
o=[]
for i in j:
     if i in v:
          o.append(i)
o=[i for i in j if i in v]   '''  

''''
s='python programming language'
l=[]
for i in s:
    if i.islower():
        l.append(i)
l=[i for i in s if i.islower()] 
'''       
'''l=[1,2,3,40,0,7,0,8,9,0,0,5,0,0,0,6]
res=[]
for i in l:
    if i%1!=0:
        i.append(i)
res=[i for i in l if i!=0]'''

'''s='123456hfdgljbgfelnfd87456987908u4y5y'
l=[]
for i in s:
    if i.isdigit():
        l.append(i)
    else:
        l.append(0)
print(l) 
# or in list comphernsive manner
d=[i*i for i in range(5)]            
'''
# set
s={i for i in range(5)}
print(s)
# dict
s={i:i for i in range(5)}
print(s)
#list
s=[i for i in range(5)]
print(s)
#tuple
s=tuple(i for i in range(5))
print(s)

# key and values in dict
names=['vikash','anem','maniknata','rahul']
v={i:'absent' for i in names}
print(v)
