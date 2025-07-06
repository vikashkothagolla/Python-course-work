

# runtime polymorphism it can be achieved by methid overridding

class Demo:
    def add(self):
        a=10
        b=90
        print(a,b)
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)       
obj=Demo()        
obj.add(100,200,300)



# compile polymorphism it can be achieved by methid overloading

class Parent:
    def transport(self):
        print("cycle")
class Child(Parent):
    def transport(self):
        print("Bike")
c=Child()
c.transport()                