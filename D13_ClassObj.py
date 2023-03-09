"""
#1. class, methods, objects
class MyClass():
    a,b=10,20       #default values
    def add(self):      #1st arg must be self
        print(self.a + self.b)
    def largerval(self):
        print("Larger value is",self.a if self.a>self.b else self.b)
c= MyClass()    #c is obj
c.add()
c.largerval()
print(c.a+c.b)


#2. conversion of local variables to class level variables
class MyClass():
    def values(self,val1,val2):
        print(val1)
        print(val2)

        self.val1 = val1    # conversion of local variables to class level
        self.val2 = val2
    def add(self):
        print(self.val1 + self.val2)
c=MyClass()
c.values(3,4)
c.add()



#3. lacal-class-global vari
a,b = 100,200   #global
class MyClass():
    a,b= 10,20      #class
    def add(self,a,b):
        print(a+b)      #will add 3,3
        print(self.a + self.b)    #will add 10,20
        print(globals()['a']+globals()['b']) #will add 100.200

    def disp(self):
        print("gM")

c = MyClass()
c.add(3,3)      #local variables
c.disp()
MyClass().disp()    #another way of calling methods - nameless object

c1 = MyClass()
c1.disp()

c.a=40  #assigning diff value 
print(c.a)

print(c1.a)     #accessing class value


"""
#4. id, is , is not
class MyClass():
    pass
c1 = MyClass()
c2 = MyClass()
c3 = MyClass()
c3 = c1

print(id(c1))   #id - address
print(id(c2))
print(id(c3))

print(c1 is c2)
print(c1 is c3)
print(c1 is not c2)
print(c1 is  not c3)
print(c1 is c2)








        
