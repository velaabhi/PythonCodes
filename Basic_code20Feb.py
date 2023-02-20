"""
#Input a number -
n = input("Enter a number")
print(n)


#swapping number -
a,b = 10,20
print("Before swapping values are ",a,b)
a,b = b,a
print("Swapped values are ",a,b)

#listing of keywords-
import keyword
print(keyword.kwlist)


print("hi \"Amit\"sir")
print("hi \Amit\'sir")
print("hi \\Sachin\\sir")
print("hi\tSAchin\tSir")


#type function-
eid= 11
ename = "ABhi"
esal= 22.3
print(type(eid))
print(type(esal))
print(type(ename))



#single line code and diff ways to init-
a,b,c=10,20,30
print(a+b+c)

a=b=c=10
print(a+b+c)


#concat using '+'   -
print(10+20)
print("Manish"+"MAnish")
print(10.23+20.42)
print(True + True)
print(10+True)  #True=1
print(10.5+False)   #False=0
print(10+10.5)


#deleting variable-
a=10
print(a)
del a
print(a)


#separator-
print(1,2,3,4,5, sep ='#')
"""

#Printing data in diff formats
eid, ename, esal = 1,"Abhi", 100000.25
print(eid)
print(ename)
print(esal)
print("Emp Id = ",eid)
print("Emp Name = ",ename)
print("Emp sal = ",esal)
print( "Emp Id = ",eid,"Emp Name = ",ename,"Emp sal = ",esal )

