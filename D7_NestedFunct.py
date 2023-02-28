#1. Nested funct
def outer():
    print("Outer funct")
    def inner():
        print("Inner funct")
    inner()
outer()


#2.Inner funct can access outer funct variable
def outer():
    print("Outer funct")
    name1="amit"
    def inner():
        print("Inner funct")
        name2="anu"
        print(name1)
        print(name2)
    inner()
    print(name1," is out of inner funct")
outer()


#3.Outer funct can access inner funct variable- nonlocal keyword
def outer():
    print("In outer funct")
    name1="Amit"
    def inner():
        nonlocal name1
        name1="durga"
        print("I am in inner func",name1)
    inner()
    print("in outer funct = ",name1)
outer()


#4.Outer funct can access inner funct variable- global keyword
def outer():
    print("In outer funct")
    name1="Amit"
    def inner():
        global name2
        name2="durga"
    inner()
    print("inner func variable called by using global keyword  ",name2)
    print("in outer funct variable  ",name1)
outer()


#5. Default arg- not passing any arg to funct, default values are considered
def empdetails(eid=1, ename="anu", esal=10000):
    print("Emp id = ",eid)
    print("Emp name = ",ename)
    print("Emp sal = ",esal)

empdetails()
empdetails(111)
empdetails(333,"durga",1020)


#6. Keyword/Named arg- mapping of keywords with values, order need not be maintained while calling the funct
def emp(name,role):
    print(name,role)
emp(name="abhi", role="tester")
emp(role="dvpr", name="vela" )



#7. Variable arg- *varargs

def variLenArgs(*varargs):
    for i in varargs:
        print(i)
    print("In varLenArgrs funct")

print("In main")
variLenArgs(10,20,30,40)

print("------------------")
variLenArgs(10,2.45)
print("In main------")


#8. None- its a special constant which doesnt mean 0, false or [ ]
def add():
    a=10
    b=20
    c=a+b   #not returning anythingm so interpreter will return None constant
x=add()
print(x)

def add(a):
    if(a%2==0):
        return True
x=add(3)
print(x)
