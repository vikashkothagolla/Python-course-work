# shortest form of function => normal way
n=9
if n%2==0:
      print("even")
else:
      print("Odd")

# using functions
def evenorodd(n):
     if n%2==0:
        print("Even")
     else:
          print("odd")
evenorodd(3)
evenorodd(8)

# using lambda
evenorodd_lambda=lambda n: "even" if n%2==0 else "odd"
print("evenorodd",evenorodd_lambda(67))



# squares of number
def squares(n):
    print(n*n)
squares(3)
squares(15) 
# using lambda
squares_lambda=lambda n:n*n
print(squares_lambda(9))


# list of square 
def sqa(l):
    for i in range(len(l)):
        l[i]**=2
    print(l)
sqa([1,6,4,5,7]) 
# using lambda
sqa_lambda=list(map(lambda i : i*i,[1,2,3,4,5]))
print(sqa_lambda)



# add of two numbers
def add(a,b):
    print(a+b)
add(78,90)
# lambda
add_lambda=lambda  a,b: a+b
print(add_lambda(23,25))


# lambda syntax
var=lambda arg: e


# upper case of python programming
squ_lambda=list(map(lambda i:i.upper(),"python programming"))
print("squ_lambda",squ_lambda)

#ASCII value of python programming
squ_lambda=list(map(lambda i:ord(i),"python programming"))
print("squ_lambda",squ_lambda)

# vowels are replaced with * in  python programming
v='aeiou'
squ_lambda=list(map(lambda i:'*' if i in v else i ,"python programming"))
print("squ_lambda",squ_lambda)

# upper case of python programming
squ_lambda=list(map(lambda i:i.upper(),"python programming"))
print("squ_lambda",''.join(squ_lambda))

#
squ_lambda=list(map(lambda i:i.title(),"python programming"))
print("squ_lambda",squ_lambda)


#
data={'vikas':35,'anem':89,'sanjay':100}
sorted_data=dict(sorted(data.items(),key= lambda i:i[1]))
print(sorted_data)


# reverse high to low values
data={'vikas':35,'anem':89,'sanjay':100}
sorted_data=dict(sorted(data.items(),key= lambda i:i[1],reverse=True))
print(sorted_data)

# max of two numbers using lambda
maxnumber=lambda a,b: a if a>b else b
print(maxnumber(90,1))
print(maxnumber(89,566))

# multiplicatioin of 2 numbers
mulnumber=lambda a,b: a*b
print(mulnumber(90,898989))


# soretd values in ascending
s=sorted([(11,2),(2,1),(1,9)],key=lambda i:i[1])
print(s)

# last character sorted in alphabetic order
l=['vikash','ram','anem','lokesh','anudeep']
s=sorted(l,key=lambda i:i[-1])
print(s)
    
# last number in list sorted by using lambda 
l=[[11,22,6556],[90,87,56],[33,766,121]]
s=sorted(l,key=lambda i:i[-1])
print(s)   

# even or odd using lambda fuction
l=[1,2,3,45,5,6,9,8]
e=list(filter(lambda i:i%2==0,l))
print(e)

# remove zeros using lambda fuction
l=[1,0,2,0,3,0,45,0,0,0,5,6,9,0,0,8]
e=list(filter(lambda i:i!=0,l))
print(e)

# filter()used in real worlds
data={
    'lap1':{'avail':True,'price':90999,'color':'blue'},
    'lap2':{'avail':False,'price':99,'color':'green'},
    'lap3':{'avail':True,'price':9999,'color':'blue'},
    'lap4':{'avail':False,'price':9,'color':'yellow'},
    'lap5':{'avail':True,'price':909,'color':'blue'},
    'lap6':{'avail':False,'price':999,'color':'green'},
    }
l=list(filter(lambda i:data[i]['avail'],data))

price=list(filter(lambda i:data[i]['price']<90000,data))
color=list(filter(lambda i:data[i]['color']=='green',data))
print(l,price,color)


