''' # read mode try:
    file=open('hr-data.txt','r')
except FileNotFoundError:
    print("file is not present")
else:
    read=file.read()
    file.seek(0)
    readlines=file.readlines()
    file.seek(0)
    readline=file.readlines()
    print(f"\nFile Content using read():\n{read}")
    print(f"\nFile Content using readlines():\n{readlines}")
    print(f"\nFile Content using readline():\n{readline}")
    file.close()
finally:
    print("Rest of the code")'''

try:
    file=open('data.txt','w')
except FileNotFoundError:
    print("file  not is present")
else:
    file.write("monday we have exam")
    file.close()
finally:
    print("Rest of the code")    


# append mode ,if want ap
try:
    file=open('data.txt','a')
except FileNotFoundError:
    print("file  not is present")
else:
    file.write("monday we have exam")
    file.close()
finally:
    print("Rest of the code")  


# write plus read
try:
    file=open('data.txt','w+')
except FileNotFoundError:
    print("file  not is present")
else:
    file.write("monday we have exam")
    file.seek(0)
    print(file.read())
    file.close()
finally:
    print("Rest of the code") 


'''# file operationas
r=>read
w=>write
a=>append
r+=>read and write
w+=> write and read
a+=> append and read'''


'''# other way to read a file
with open('data.txt','r+') as file:
          file.write('\nFile operations')
          file.seek(0)
          print(file.read())'''
 # check
import os
print(os.getcwd()) # cureent working dirctory
if not os.path.exists("DSDA"): # its for checkig where the DSDA is there or not there in the systam
    os.mkdir("DSDA") # mkdir=make a directory

# remove
import os

if os.path.exists("DSDA"): # its for checkig where the DSDA is there or not there in the systam
    os.rmdir("DSDA") # rmdir=remove a directory, if that file has no data only it will remove,i.e  the file should be empty,other wise it won't will work

# create folder inside folder we use "makedirs"
import os

if not os.path.exists("DSDA"): # its for checkig where the DSDA is there or not there in the systam
    os.makedirs("DSDA/12324") # mkdir=make a directory



# removing
import os
import shutil
if  not os.path.exists("DSDA"):
    os.mkdir("DSDA")
    os.makedirs("DSDA/12324")
shutil.rmtree("DSDA")    

# list out dirctories in our system
import os
os.listdir.'.'