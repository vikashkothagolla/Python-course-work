'''class Human: # class
    def __init__(self,name,age): #constryctor
        self.name=name  # attr/propetirs
        self.age=age
    def run(self): # functions/methods
        print("runnning")
    def walk(self):
        print("walking")
my_human=Human("ramana",6) # object creation
print(my_human.age) # accesing  attr/proper
print(my_human.name)
my_human.run() # calling methods
my_human.walk()
'''
'''# oops basic questions
class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def diplay(self):
        print(self.title,self.author,self.price)
book=Book("sansrikit","vedhavaysaudu",560,)
book.diplay()'''            

# employ salary
class Employ:
    def __init__(self,name,basesalary):
        self.name=name
        self.basesalary=basesalary
    def annualsalary(self):
        return self.basesalary*12
emp=Employ("ram",90)
print(emp.annualsalary())


# student grade
def is_passed(self):
avg = sum(self.marks) / len(self.marks)
return avg >= 40