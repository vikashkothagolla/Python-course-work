'''class Father:
    def fdisplay(self):
        print("father")
class Mother:
    def mdisplay(self):
        print("mother")
class Child(Father,Mother):
    def cdisplay(self):
        print("Child")
c=Child()
c.cdisplay()                       
c.mdisplay()
c.fdisplay()

f=Father()
f.fdisplay()

m=Mother()
m.mdisplay()'''


# whatsup status => multiple inheritance
class A:  # class creation
    def display_a(self): # fuc/methods
        print("Parent Class")
class B: 
    def display_b(self): # fuc/methods
        print("Parent class")
class C:
    def display_c(self): # fuc/methods
        print("Parent class")
class D(A,B,C):
    def display_d(self): # fuc/methods
        print("Child class A,B,C->D")        


d=D()  # object creation
d.display_a()  # calling method/function
d.display_b() # calling method/function
d.display_c() # calling method/function
d.display_d() # calling method/function


# Definition: One parent class and one child class. The child inherits from only one parent(single inheritance)
# in this we have (multiple) parents and single child it is called multiple inheritance
# Definition:(Multilevel Inheritance)Inheritance in a chain — a class is derived from another derived class.
# (Hierarchical Inheritance) Definition: Multiple child classes inherit from the same single parent class.
# (Hybrid Inheritance) Definition: A combination of two or more types of inheritance.

'''parent adn child have same method we use super()
to extract information from paernt clas to child cls we use super()
super can ocuur only we single child and parent'''
