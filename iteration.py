"""x=int(input("Enter min number:"))
y=int(input("Enter max number:"))
for i in range(x,y+1):
    if(i%2!=0):
        print(i)
"""


"""for i in range(50,71):
    print(i)

"""

"""
lst=[1,2,3,4,5]
prod=1
for i in lst:
    prod=prod*i
print(prod)  
"""
"""
x=int(input("Enter a number for generating a table :"))

for i in range(1,11):
    print(x,'x',i,'=',i*x)
"""

'''
lst=[3,6,5,12]

for i in lst:
    if(i==5):
        break
    
    print(i)
'''

'''
x=0
while x<20:
    x+=1
    if x%3==0:
        continue
    print(x)
'''

'''
#assert
x=int(input("Enter a number greater than 10:"))
assert x>10, "Wrong number entered"
print("You entered ",x)
'''

'''
x=int(input("Enter a number please :"))
for i in range(x):
    if(i%10==0):
        continue
    if(i>100):
        break
    print(i)
'''

#prime

'''
x= int(input("Enter your number :"))
primeFlag=True
for i in range(2,x):
    if x%i==0:
        primeFlag=False
if primeFlag==True:
    print("Prime No.")
else:
    print("Not a prime No.")
'''
