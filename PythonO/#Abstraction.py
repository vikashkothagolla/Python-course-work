
from abc import ABC, abstractmethod
class Bankaccount(ABC):
    def deposit(self):
        print('you can deposit the amount')
    def checkbalance(self):
        print('ypu can check your balance')

    @abstractmethod
    def withdraw(self):
        pass
    def viewhistory(self):
        print('you can check the history')

class CurrentAccount(Bankaccount):
    def withdraw(self):
        print('You can withdraw Extra amount')

class SavingAccount(Bankaccount):
    def withdraw(self):
        print('You can withdraw the amount')

mani=CurrentAccount()
shanmukh=SavingAccount()
mani.checkbalance()
mani.deposit()
mani.viewhistory()
mani.withdraw()
shanmukh.checkbalance()
shanmukh.deposit()
shanmukh.viewhistory()
shanmukh.withdraw()



# 
from abc import ABC, abstractmethod
class Order(ABC):
    @abstractmethod
    def processor_order(self):
        pass
class foodorder(Order):
    def processor_order(self):
        print("Processing Food order:check availability,estimate time")
class GroceryOrder(Order):
    def processor_order(self):
        print("proceesing grocery order:check inventry time")
class MedicineOrder(Order):
    def processor_order(self):
        print("Processing Medicine order:valid presricption")
