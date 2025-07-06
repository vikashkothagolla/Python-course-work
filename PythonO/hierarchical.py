class Parent:
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
s.pdisplay()          # Output: parent class (inherited)








































































