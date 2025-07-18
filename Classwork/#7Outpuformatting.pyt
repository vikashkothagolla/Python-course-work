# output formatting
a='vikash yadav'
print(a)
print(a[::-1])

name="vikash"
school="krrs"
Score=85
print("Name:" , name, "School:", school)
print('2025','07','09',sep="-")
print(name,end=" ")
print(school)
print("name \n school")
print("name \t school")
print("name: %s | school: %s | score: %d " % (name, school, Score))
print(f"name:{name} | score:{Score} | School:{school}")

#if and else
items=['car','bike','scooty']
print("welcome to flipcart".center(80,'-'))
searchitem=input("enter the item: ").lower()

if searchitem in items:
    print("found ")
else:
    print("not found")    

# if ,elif and else
amo=int(input('enter amount'))
if amo>50000:
    print("go to goa")
elif amo>25000:
    print("go to shopping")
elif amo>15000:
    print("got to maintaince")
else:
    print("save amount")               

    