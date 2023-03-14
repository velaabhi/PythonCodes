"""
#1. conver of local to class values
class Myclass:
    def __init__ (self,v1,v2):
        print(v1)
        print(v2)

        self.v1  = v1
        self.v2 = v2

    def add (self):
        print(self.v1+self.v2)

c =  Myclass(10,20)
c.add()


#2.
class Myclass:
    pass
c=Myclass()
print(c)        #addr of obj c


#3.
class Test:
    def __str__ (self):
        return "Welcome to __str__() Constructor"
t= Test();
print(t)


#4.
class Test:
    def __str__(self):
        return 10       #cannot pass int, it accepts string only
t = Test()
print(t)


#5. Simple inheritance
class Person:       #base class
    name = 'ABC'
    no = 8149969019
class address(Person):  #child class
    address = 'Pune'
p=address()     #creating obj of address class
print(p.name)
print(p.no)
print(p.address)

"""
#6. Simple inheritance

class Parent:
    def m1(self):
        print("Parent cl m1")

class Child(Parent):
    def m2(self):
        print("Child cl m2")
p = Parent()
p.m1()
#p.m2()     will give error cz parent cannot access child method

c= Child()
c.m1()
c.m2()
























    


















