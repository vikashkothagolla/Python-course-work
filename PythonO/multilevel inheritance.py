class Grandparent:
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
gp.gpdisplay()
