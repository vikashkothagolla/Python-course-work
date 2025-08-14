'''class Grandparent:
    def gpdisplay(self):
        print("grandparent")

class Parent(Grandparent):  # Parent inherits from Grandparent
    def pdisplay(self):
        print("parent")

class Child(Parent):  # Child inherits from Parent
    def cdisplay(self):
        print("child")

# Object creation
c = Child()

# Calling methods from all three classes
c.cdisplay()    # Output: child
c.pdisplay()    # Output: parent
c.gpdisplay()   # Output: grandparent

p=Parent()

p.pdisplay()
p.gpdisplay()

gp=Grandparent()
gp.gpdisplay()'''



# whatsup status => multilevel inheritance
class A:  # class creation
    def display_a(self): # fuc/methods
        print("Parent Class")
class B(A): 
    def display_b(self): # fuc/methods
        print("Parent class")
class C(B):
    def display_c(self): # fuc/methods
        print("Parent class")
class D(C):
    def display_d(self): # fuc/methods
        print("Child class A,B,C->D")        


d=D()  # object creation
d.display_a()  # calling method/function
d.display_b() # calling method/function
d.display_c() # calling method/function
d.display_d() # calling method/function



super() is used in differnt clases