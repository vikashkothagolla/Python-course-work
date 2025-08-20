

'''# runtime polymorphism it can be achieved by methid overridding
class Demo:
    def add(self):
        a=10
        b=90
        print(a,b)
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)       
obj=Demo()        
obj.add(100,200,300)
# compile polymorphism it can be achieved by methid overloading it is not possible 
class Parent:
    def transport(self):
        print("cycle")
class Child(Parent):
    def transport(self):
        print("Bike")
c=Child()
c.transport()'''              



# polymorphism:same mehtod but it acts different


class Normaluser:
    def __init__(self,username):
        self.username=username
        print(f'\nWelcome to the youtube\n{self.username} account is created')
    def playvideo(self):
        print("ads include")
        print("video with low quality")
        print("no yt music")
        print("free of cost")
    def profile(self):
        print("you can upload your profile")
    def likes(self):
        print("you the like the cintent")
    def share(self):
        print("you share the cintent")

class premiumuser(Normaluser):
    def __init__(self,username):
        super().__init__(username)
    def playvideo(self):
        print("No ads")
        print("high video quality")
        print("with yt music")
        print("with background play")
        print("high price")                                
vikash=Normaluser("Vikash")
vikash.playvideo()
vikash.profile()
vikash.likes()
vikash.share()


ram=premiumuser("Ram")
ram.playvideo()