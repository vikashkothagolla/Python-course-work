'''# inheritance 20
class Device:
    def power_off(self,power_off):
        print("The power is off")
class Laptop(Device):
    def openvscode(self):
        print("the decvice opened vscode ide")
lap=Laptop()
lap.power_off("OFF")
lap.openvscode()           

# inheritance 19 teacher and subject teacher
class Teacher:
    def __init__(self,name):
        self.name=name
    def teach(self):
        print(f"{self.name} teaches general subjects")
class SubjectTeacher(Teacher):
    def teach(self):
        print("the teaher teaches the mathametics subject")
tea=SubjectTeacher("RAVANAIAH")
tea.teach()

# inheritance 18 Vehicle and Bike
class Vehicle:
    def drive(self):
        print("Driving")
class Bike(Vehicle):
    def wheel_count(self):
        print("2 wheelers")
veh=Bike()
veh.drive()
veh.wheel_count()          

# inheritance 17 Member and PremiumMember
class Member:
    def __init__(self,name):
        self.name=name
    def benefits1(self):
        return "basic access"
class PremiumMember(Member):
    def benefits(self):
        return "freedevivery + unliitedcontent"
mem=PremiumMember("vikash")
print(mem.benefits())     
print(mem.benefits1())

# inheritance 16 appliance and washing machine
class Appliance:
    def __init__(self,name):
        self.name=name
class WashingMachine(Appliance):
    def washclothes(self):
        print(f"{self.name} is a super electronic")
app=WashingMachine("ifb")
app.washclothes()   '''

# polymorphism 30 Document EXporters
'''class Vikash:
    pass
object= Vikash()
print("this is vikash yadav")

class Document:
    def export(self):
        print("documnet")        
class PDFEXPORTER(Document):
    def export(self):
        print("this exporying as pdf")
class CSVEXPORTER(Document):
    def export(self):
        print("This is export Csv documnet")
for ExporterClass in [PDFEXPORTER, CSVEXPORTER]:
    exporter = ExporterClass()  # create an instance
    exporter.export()  


# poly 29 Transport Booking
class Transport:
    def book(self):
        pass
class Train(Transport):
    def book(self):
        print("the train ticket  is bookoing is conformed")
class flight(Transport):
    def book(self):
        print("the Flight ticket  is bookoing is conformed") 
def booking(service):
    service.book()
booking(flight())
booking(Train())      

# poly 28 Employe
class Employ:
    def role(self):
        pass
class writer(Employ):
    def role(self):
        print("he will write")
class dop(Employ):
    def role(self):
        print("this the dop")
def employee(depat):
    depat.role()
employee(dop())
employee(writer())


# poly 27 Media Player

class Media:
    def play(self):
        pass
class AUdio(Media):
    def play(self):
        print("audio media")
class Video(Media):
    def play(self):
        print("Video player")
mediaplayer=[AUdio(),Video()]
for i in mediaplayer:
    i.play()                 


# poly 26 LOgin

class LoginSystem:
    def login(self):
        pass
class adminlogin(LoginSystem):
    def login(self):
        print("admin is loging")
class userlogin(LoginSystem):
    def login(self):
        print("login by user")
loginsys=[adminlogin(),userlogin()]
for i in loginsys:
    i.login()


# poly 25 Vehicle Sounds
class vehiclesound:
    def sound(self):
        pass
class lorry(vehiclesound):
    def sound(self):
        print("the sound poo poo")
class bus(vehiclesound):
    def sound(self):
        print("the sound is like dhomma dhoom")
Sound=[lorry(),bus()]
for i in Sound:
    i.sound()    


# poly 24 Shape Areas
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def area(self):
        return 22/7*9*9
class Square(Shape):
    def area(self):
        return 8*8
s1=Circle()
s2=Square()
print(s1.area())
print(s2.area())

# poly 23 Message Sender

class MessageSender:
    def send(self):
        pass
class Whatsapp(MessageSender):
    def send(self):
        print("the message sender is whatspp")
class email(MessageSender):
    def send(self):
        print("the message sender is email")
def msgsender(service):
    service.send()
msgsender(Whatsapp())
msgsender(email())'''    





