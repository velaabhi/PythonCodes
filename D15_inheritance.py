"""
#1.hybrid inherit
class School:
    __sch = "abc"   #private mem not accessible outside
    schName ="DPS "   # publc method
class Stud1(School):    #simple inher
    def fun2(self):
        print("funct in student 1 ")
class Stud2(School):    #muli level inher
    def fun3(self):
        print("funct in student 1 ")

class Stud3(Stud1, School):
    def fun4(self):
        print("funct in student 1 ")


obj = Stud3()
obj.fun4()
obj.fun1()
obj.fun2()
print(obj.sch)
print(obj.schName)


#2. method overriding

from math import pi
class Shape:
    def __init__(self,name):
        self.name = name
    def area(self):
        pass
    def __str__ (self):
        return self.name

class Square(Shape):    #inheritance
    def __init__ (self,length):
        super().__init__("Square")  #calling super constr
        self.length = length
    def area(self):
        return self.length**2


class Circle(Shape):    #inheritance
    def __init__ (self,radius):
        super().__init__("Circle")  #calling super constr
        self.radius = radius
    def area(self):
        return pi*self.radius**2

a = Square(4)       #creTING OBJ
b = Circle(6)
print(a)
print(b)

print(a.area())
print(b.area())


"""
#3.Abstract class

from abc import ABC, abstractmethod

class AbstractDemo(ABC):    #abstraction
    @abstractmethod         #decorator
    def display(self):
        none

class Demo(AbstractDemo):       #inheritance
    def display(self):
        print("Abstract method ")

#obj1 = AbstractDemo()
obj = Demo()
obj.display()



























        


















