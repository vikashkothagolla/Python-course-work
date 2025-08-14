

'''#  inheritanc ebu yt
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
dobject.display()     # calling fun/methods'''
 



# whatsup status => single inheritance
class A:  # class creation
    def display_a(self): # fuc/methods
        print("Parent Class")
class B(A):
    def display_b(self):
        print("child Class")
a=A() # object creation
a.display_a() # calling method/function

b=B()  # object creation
b.display_b()  # calling method/function
b.display_a()  # calling method/function
# by using child cls we can access the parent cls it is called single inheritance 
 
