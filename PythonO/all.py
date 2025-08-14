# single inheritance
# single parent and single child
class Parent:
    def speak(self):
        print("I am the parent")
class Child(Parent):
    def play(self):
        print("I am the child")
Object=Child()
Object.speak()
Object.play()        


# multiple inheritance
# multiple parents with single child
class Parent1:
    def method1(self):
        print("I am the parent")
class Parent2:
    def method2(self):
        print("I am also the parent")
class Child(Parent1,Parent2):
    def method3(self):
        print("I am the child")
object=Child()
object.method1()
object.method2()
object.method3()




# Multilevel Inheritance :Definition:(Multilevel Inheritance)Inheritance in a chain — a class is derived from another derived class.
class GrandParent:
    def method1(self):
        print("I am the geandparent")
class Parent(GrandParent):
    def method2(self):
        print("I am the parent")
class child(Parent,GrandParent):
    def method3(self):
        print("I am the child")
object=Child()
object.method1()
object.method2()
object.method3()        


# Heirarchical Inheritance: Multiple child classes inherit from the same single parent class.

class Parent:
    def method1(self):
        print("I am the parent")
class Child1(Parent):
    def method2(self):
        print("I am the Child1")
class Child2(Parent):
    def method3(self):
        print("I am the child2")
object=Child2()
object.method3()
object.method1() 
object=Child1()
object.method2()
object.method1()
object=Parent()
object.method1()
