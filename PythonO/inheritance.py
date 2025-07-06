class baseclass:  # class creation
    a=10          # attr/prop
    b=20
    def display(self):  #functions/methods
        print("baseclass")
class derivedclasss(baseclass):
    c=90
    d=100
    def show(self):
        print("derivedclass")
dobject=derivedclasss()    # object creation
print(dobject.c,dobject.d) # accesing attr/properties
dobject.show()    # calling method/function
print(dobject.a,dobject.b) # accesing attr/properties
dobject.display()     # calling fun/methods
 