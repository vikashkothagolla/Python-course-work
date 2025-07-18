num=int(input("enter the table number:"))
for i in range(1,21):
    print(f"{num}*{i}={num*i}")

# wwdwdwdd
s='Varun','Charan','Ram','Akhilesh'.lower()
n=len(s)
ch=input("Enter the char: ").lower()
for i in range(n):
    if s[i]==ch:
        print(ch,i)
#fddddddg
products=['bike','cycle','car','laptop','watch']
items=input("enter the items: ").split()
for i in items:
    if i in products:
        print(products.index(i),i)
    else:
        print(f"{i} is not available")

# while
email,password='ml123@gmail.com','hsi'
useremail=input("enter the email:")
password=input("enter the password:")
max_att=5
while max_att>0:
    useremail=input("enter the email:")
    password=input("enter the password")
    if useremail==email and password==password:
        print("login successful:")
        break  
    else:
        print('Ivalid login')
    max_att-=1
else:
    print("Try after some time:")    


