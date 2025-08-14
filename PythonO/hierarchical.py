'''class Parent:
    def pdisplay(self):
        print("parent class")

class Daughter(Parent):  # Inheriting from Parent
    def ddisplay(self):
        print("daughter class")

class Son(Parent):  # Inheriting from Parent
    def sdisplay(self):
        print("son class")

# Parent object
p = Parent()
p.pdisplay()          # Output: parent class

# Daughter object
d = Daughter()
d.ddisplay()          # Output: daughter class
d.pdisplay()          # Output: parent class (inherited)

# Son object
s = Son()
s.sdisplay()          # Output: son class
s.pdisplay()          # Output: parent class (inherited)'''

# single parent multiple childs 
class A:  # class creation
    def display_a(self): # fuc/methods
        print("Parent Class")
class B(A): 
    def display_b(self): # fuc/methods
        print("Parent class")
class C(A):
    def display_c(self): # fuc/methods
        print("Parent class")
class D(A):
    def display_d(self): # fuc/methods
        print("Child class A,B,C->D")   

b=B()
b.display_a()
b.display_b()


c=C()
c.display_a()
c.display_c()


d=D()
d.display_a()
d.display_d()































































