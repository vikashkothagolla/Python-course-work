class Father:
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
m.mdisplay()