
#1. Built in func 
print(round(1.648,1))   #round funct

seq_range=range(5,9)
print(list(reversed(seq_range)))


#2.User defd funct - display
def disp():         #declaration
    print("Good Morning")   # defination
disp()          #call


#3.User defd funct - sum of 2 nos
def sum(x,y):   
    res=x+y
    print(res)
a=int(input("Enter 1st no"))
b=int(input("Enter 2nd no"))
sum(a,b)
print("back in main")

#4.User defd funct - print seq
def printSeq(i):
    for x in range(i):
        print("HI ",x)
i=int(input("Enter a no"))
printSeq(i)


#5.User defd funct - Sqr w/o return
def Sqr(n):
    res= n*n
    print("Square is ",res)
Sqr(5)



#6.User defd funct - Sqr with return
def Sqr(n):
    res= n*n
    return res
sq= Sqr(5)
print("Square is ",sq)



#7.User defd funct - accept range and cube all the items
def CubeRange(l,u):
    for x in  range (l,u+1):
       # print("Cube is ",(x*x*x))
       z= x*x*x         #try with return
    return z
a=int(input("Enter lower  no"))
b=int(input("Enter upper  no"))
c= CubeRange(a,b)
print(list(c))



#8.User defd funct - nested funct
def hbday(person):              #funt2
    print("Happy Bday dear ",person)

def main():                     #funct1
    hbday("Amit")
    hbday("Anu")

print("Welcome to bday msgs")
main()                      #calling main funct
print("End of code")


#9.User defd funct - simple calc
def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def prod(a,b):
    return a*b

def division(a,b):
    if(a==0 or b==0):
        print("Division cannot be performed cz")
        return 0
    else:
        return a/b

n1=int(input("Enter 1st  no"))
n2=int(input("Enter 2nd  no"))

add=sum(n1,n2)
print("Addition of 2 nos is ",add)

diff=sub(n1,n2)
print("Subtraction of 2 nos is ",diff)

mul=prod(n1,n2)
print("Multiplication of 2 nos is ",mul)

div=division(n1,n2)
if div==0:
    print("values are invalid")
else:
    print("Division of 2 nos is ",div)


#10.User defd funct - Local and Global variables
x,y = 10,20     #global vari


def add(a,b):   #local vari
    print(a+b)
    print(x+y)

def mul(a,b):
    print(a*b)
    print(x*y)

print("Start")
add(4,4)
mul(5,5)
print("Stop")


#11.User defd funct - globals keyword for variables with same name in local and global
a,b = 10,20
def add(a,b):
    print(a+b)      #local variables are considered
    print(globals()['a']+globals()['b'])    #global vari are considered
add(3,4)
