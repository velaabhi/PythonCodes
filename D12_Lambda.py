"""
#1. lambda
def m1(x,y):
    print(x*y)
m1(10,20)

a = lambda x,y : x*y
print(a(10,20))

b = lambda x,y : x if x>y else y
print(b(3,4))


#2. filter
n = 'Yogesh'
print(list(filter(lambda x:x == 'e', n)))


n = 'purple'
print(list(filter(lambda x:x == 'p', n)))

#2. map

print(list(map(lambda x:x*2 , range(10))))


#3. Module
import math
print("Value of pi is ", math.pi)

import math as m        #using alias
print("Value of pi is ", m.pi)



#4. importing calc module
import calc
calc.addition(10,20)
calc.subtraction(20,10)

print(dir(calc))


#4. importing calc module
import datetime as dt
print(dt.datetime.now())
print(dt.date.today())


#5. decorators
def makeDecorator(func):
    def inner():
        print("I am decorator ")
        func()
    return inner    #call to inner function

@makeDecorator  #the function which is to be decorated(wrapped) use @ wrapper/decorator
                    #function name above its defination
def genralFunc():       #funct to be decorated
    print("i am general func")

genralFunc()        #main line




#6. decorators uppercase

def uppercase(func):        #2nd
    def wrapper():          #4th
        original_res = func()          #5th
        modified_res = original_res.upper()     #6th
        return modified_res         #7th
    return wrapper          #3rd

@uppercase
def greet():
    return  'Hello Guys'
print(greet())          #1st

"""
#7. decorators uppercase and split

def uppercase(func):        #2nd
    def wrapper():          #4th
        original_res = func()          #5th
        modified_res = original_res.upper()     #6th
        return modified_res         #7th
    return wrapper          #3rd

def split_string(func):
    def wrapper():
        func_data = func()
        splited_res = func_data.split()
        return splited_res
    return wrapper

@split_string
@uppercase
def greet():
    return  'Hello Guys'
print(greet())          #1st



        






