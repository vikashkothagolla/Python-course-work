class Human: # class
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

