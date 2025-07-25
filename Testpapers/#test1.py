date,month,year=input().split('-')
print(f'{year}/{month}/{date}')


n=int(input())
if n%2==0:
    print("Even Winner")
else:
    print("Odd Winner")
    


s=input().lower()
print(s.translate(str.maketrans('aeiou','*****')))


l=list(map(float,input().split()))
print(sum(l))
print(max(l))

credentials = ("admin", "python123")
username=input()
password=input()
if credentials[0]==username and credentials[1]==password:
    print("Login Successful")
else:
    print("Access Denied")



names=set(input().split(','))
print(sorted(names))


sen=input().split()
for i in sen:
    print(i[::-1],end=' ')


l=list(map(int,input().split()))
while (0 in l):
    l.remove(0)
print(l)

l=list(map(int,input().split()))
res=[]
for i in l:
    if i!=0:
        res.append(i)
print(res)


line=input()
data={}
for i in line:
    if i not in data and i!=' ':
        data[i]=line.count(i)
print(data)

n=int(input())
data={}
max_val=0
res_name=''
for _ in range(n):
    name,marks=input().split()
    marks=int(marks)
    if marks>max_val:
        max_val=marks
        res_name=name
        
    data[name]=marks

print(data)
print(res_name)

