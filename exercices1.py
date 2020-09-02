# 1
'''
def p(x,y):

     sum=x+y
     if (x*y)>1000:
         return sum
     else:
         return x*y


result = p(30,40)
print(result)

'''

#2
'''
def sumNum(num):
    previousNum = 0
    for i in range(num):
        sum = previousNum + i
        print("Current Number", i, "Previous Number ", previousNum," Sum: ", sum)
        previousNum = i

print("Printing current and previous number sum in a given range(10)")
sumNum(10)

'''


#3

'''
def printEveIndexChar(str):
  for i in range(0, len(str)-1, 2):
    print("index[",i,"]", str[i] )

inputStr = "pynative" 
print("Orginal String is ", inputStr)

print("Printing only even index chars")
printEveIndexChar(inputStr)
'''

#4
'''
lst=[1,5,10,2,15,8,7]

def div(lst):
    for i in lst:
        if i%5==0:
            print(i)

div(lst)

'''
#5
'''
str="Emma has some apples.Emma sells the apples"
x= str.count("Emma")

print("The word has appeared",x,"times")

'''


#6
'''
name = input("Enter your name ")
print("Your name is "+name)

age= int(input("Enter your age: "))

yearBorn = 2020-age

year100 =  yearBorn+100

print("You will be 100 years old in year",year100)

'''


#7
'''
no= int(input("Enter your number: "))

if no%2==0:
    print("Your number is even.")
    if no%4==0:
        print("Your number is a multiple of 4.")
else:
    print("Your number is odd.")
    
'''


#8
'''
lst=[1,1,2,3,5,8,13,21,34,55,89]

lst2=[x for x in lst if x<5]

num= int(input("Enter a number: "))

lst3=[x for x in lst if x<num]

print(lst3)

'''


#9
'''
num= int(input("Enter your number: "))

lst=[]
lst=[i for i in range(1,num+1) if num%i==0]

print(lst)

'''

#10
'''
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

lst=[i for i in a if i%2==0]

print(lst)

'''


#11
'''
import random
a = random.randint(1,9)
c=0
while True:

 num= input("Enter your guess please: ")
 if num=="exit":
    print("Game has been finished")
    break
 elif int(num)<a:
    print("Number too low ")
    c+=1
 elif int(num)>a:
    print("Number too high")
    c+=1
 elif int(num)==a:
    print("You guessed correctly")
    c+=1
    break
   

print("Number of tries %d" %c)

'''

#12
'''
def getNo():
    return int(input("Enter your number: "))


def isPrime(a):
    for i in range(2,a):
        if a%i==0:
            return 1
        else:
            return 0
c=0
a = getNo()
c= isPrime(a)

if c==1:
    print("Number is not prime")
else:
    print("Number is prime")
 
'''

#13
'''
a=[5,10,15,20,25]

def listend(x):
    return [x[0],x[-1]]

print(listend(a))

'''

#14
'''
a=[2,3,3,4,5,6,1,2]

def setList(x):
    return list(set(x))

b=setList(a)

print(b)

'''

#15
'''
sentence=input("Enter sentence: ")
splitList=sentence.split()

print(splitList)
reverse=[]

i=len(splitList)

while i!=0:
    i=i-1
    reverse.append(splitList[i])
    
str1=' '.join(reverse)
print(str1)

'''


#16

