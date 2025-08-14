class login:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
        self._otp=1234
    def getpassword(self):
        return  self.__password
    def updatePassword(self,new_pwd):
        self.__password=new_pwd

    @property
    def publicotp(self):
        return self._otp
    @publicotp.setter
    def publicotp(self,new_otp):
        self._otp=new_otp
# public
print("username",vikash.username)

#private
print("Password",vikash.getpassword())

#protected
print("OTP",vikash.publicotp)
vikash.username="_vikash_"
print("Updayed username",vikash.username)

vikash.updatePassword("Vk@18")
print("Updated password",vikash.getpassword())

vikash.publicotp=1111
print("Updated OTP",vikash.publicotp)
