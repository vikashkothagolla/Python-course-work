''''# book detils
class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def displayinfo(self):
        print(self.title)
        print(self.author)
        print(self.price)
book1=Book('my madness','its me',989)
book1.displayinfo()
# emplyee salary
class Employee:
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
    def calculate_annul_salary(self):
        print(self.name)
        print(self.base_salary)
employee1=Employee("vikash",'200k')
employee1.calculate_annul_salary()'''       

'''# student grade evaluator
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_passed(self):
        avg=sum(self.marks)/len(self.marks)
        return avg>=40
s1=Student("vikash",[5,6,7])
print(s1.is_passed())'''    
'''# shape rectangle
class Shape:
    def __init__(self,color,):
        self.color=color
    def display(self):
        print(self.color)
class Rectangle(Shape):
    def __init__(self,color,width,length):
        super().__init__(color)
        self.width=width
        self.length=length
    def area(self):
        return self.length*self.width
result=Rectangle("Green",8,7)
result.display()
print("area: ",result.area())'''
'''# employ and manager
class Employ:
    def __init__(self,name):
        self.name=name
    def show_role(self):
        print("General employ")

class Manager(Employ):
    def show_role(self):
        print("Manager with team responsibilities")
mgr = Manager("Ravi")
mgr.show_role()'''

'''#order status tracker
class Order:
    def __init__(self,order_id,status="success"):
        self.order_id=order_id
        self.status=status
    def update_status(self,new_status):
        self.status=new_status
    def show_status(self):
        print(self.order_id,self.status)
o=Order("ORD5454")
o.update_status("Pending")
o.show_status()'''

'''# inventory item
class InventoryItem:
    def __init__(self,quantity,name):
        self.name=name
        self.quantity=quantity
    def update_quantity(self,amount):
        self.quantity+=amount
    def display(self):
        print(self.name,self.quantity)
item=InventoryItem(6,"keyboard")
item.update_quantity
item.display()'''        

'''# Product Discount System
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def discount_apply(self,percentage):
        self.price-=self.price*(percentage/100)
    def display(self):
        print(self.name,self.price)    
res=Product("mobile",90)
res.discount_apply(20)
res.display()'''


'''# movie rating check
class Movie:
    def __init__(self,name,rating,title):
        self.name=name
        self.rating=rating
        self.title=title
    def is_family_friedly(self):
        return self.rating<13 
res=Movie("crime",90,"Animal")
print(res.is_family_friedly())'''  

'''# odometer how much car travelled
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        self.odometer=0
    def drive(self,km):
        self.odometer+=km
    def display(self):
        print(self.odometer)
car1=Car("xyz","model s")
car1.drive(455)
car1.drive(55)
car1.display()'''        


'''# 16 codeplay
# 16 appliance and washingmachine
class Appliance:
    def __init__(self,brand):
        self.brand=brand
class WashingMachine(Appliance):
    def wash(self):
        print(f"{self.brand} wasasihng clothes")
washingmachine=WashingMachine("LG")
washingmachine.wash()'''


''' 17 member and perimumber
class member:
    def __init__(self,name):
        self.name=name
    def benefits(self):
       return "Basic access"
class Premiummember(member):
    def benefits(self):
        return "premium content + free delivery"
pre=Premiummember("vikash")
print(pre.benefits())'''

'''# 18 vehicle and car
class Vehicel:
    def drive(self):
        print("i am driving")
class Car(Vehicel):
    def wheel_count(self):
        print("4 wheelers")
c=Car()
c.drive()
c.wheel_count()'''


''' # 19 Teacher and subTeacher
class Teacher:
    def __init__(self,name):
        self.name=name
    def teach(self):
        print(f"{self.name} teaches normal subject")
class MathTeacher(Teacher):
    def teach(self):
        print(f"{self.name} teaches math subject")
t=MathTeacher("vikash")
t.teach()'''                   

''' # pass 
x = 10
if x > 5:
    pass   # TODO: handle this later
else:
    print("x is small")
# pass 
class Vikash:
    pass
object=Vikash()
print("object is created")'''

# polymorphism
# using creditcard and phonepay
class Payment:
    def pay(self,amount):
        pass
class Creditcard(Payment):
    def pay(self,amount):
        print(f"paid{self.amount} uaing credit card")
class Phonepay(Payment):
    def pay(self,amount):
        print(f"paid{self.amount} uaing phonepay")
    def checkout(payment_method):
     payment_method.pay(89)           
creditbill=Creditcard()
phoneopay=Phonepay()
