''' # (int) def update(val):
    val=val+10
    print("Inside the function:",val)
val=12
update(val)
print("Outside the function:",val) '''

''' # (float)
def update(val):
    val=val+10
    print("Inside the function:",val)
val=12.5
update(val)
print("Outside the function:",val)'''

# (string)
'''def update(val):
    val=val+"lang"
    print("Inside the function:",val)
val="python"
update(val)
print("Outside the function:",val)
# the above int,string,float are immutable so it can chnage inside the function only not the outside the function
'''

# list mutable so it can change inside the function and outside the function
'''def update(val):
    val.append(6)
    print("Inside the function:",val)
val=[1,2,3,4,5]
update(val)
print("Outside the function:",val) 
'''
# tuple immutable can effect inside the function only
'''def update(val):
    val=val+(6,7)
    print("Inside the function:",val)
val=(1,2,3,4,5)
update(val)
print("Outside the function:",val)'''

# set is mutable so it can effect inside the function and the outside the function
'''def update(val):
    val.add.(5)
    print("Inside the function:",val)
val={1,2,3,4}
update(val)
print("Outside the function:",val)'''

# dict is mutable so it can effect inside the function and the outside the function
'''def update(val):
    val[5]=25
    print("Inside the function:",val)
val={1:1,2:4,3:9,4:16}
update(val)
print("Outside the function:",val)'''# tuple immutable can effect inside the function only

# boolean immutable can effect inside the function only
'''def update(val):
    val=True
    print("Inside the function:",val)
val=False
update(val)
print("Outside the function:",val)'''
 # we passing the reference in(mutable) list,set,dict so it can change the inside the function and outside the function
 # we passing the value in9immutable) int,float,string,bool,tuple can only effect the inside the function

# here we are using shallow copy,it can change the inside the function only
'''def update(val):
    val=val.copy()
    val.append(5)
    print("Inside the function:",val)
val=[1,2,3,4]
update(val)
print("Outside the function:",val)'''