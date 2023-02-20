#block of organized, reusable code, modularity
# syntax :      def functionname( parameters ):
#                   "function_docstring" 
#                   function_suite 
#                   return [expression]W


def printme(str):
    "this func prints str arg"
    print(str)
    return
printme("First call")
print("Functin is called")
printme("2nd call")


#calling one funct into another
def hpybday(name):
    print("happy bday ",name)

def main():
    hpybday('Abhi')

main()      #calling main()


#local and global variables
a =20       #global variable
def add(a):
    b=30    #local variable
    print("Addition",(a+b))
add(a)
def mul(a):
    b=2  #local variable
    print("Mul",(a*b))
mul(a)


#Local vs. global variables: same variable name -use globals()
a,b = 10,20     #global variables
def add(a,b):
    a,b=30,40   #local variables with same name
    print("addition of locals is ",(a+b))
    print("Add of glabals is ",(globals()['a']+globals()['b']))

add(a,b)
 

#inner function - declaring function inside the another function 
def outer():
    name1="Welcome"
    def inner():
        nonlocal name1
        name1="India"

inner() #inner function calling
print(“outer Function – “, name1)
outer() # outer function calling


#Function with default arg
def empDetails(eid=1,ename="Abhi",esal=1000):
    print("Emp Id is ",eid)
    print("Emp Name is ",ename)
    print("Emp sal is ",esal)

empDetails()       #default values
empDetails(222)
empDetails(333, "Ram")
empDetails(111, "Raj", 105000)


#Function with Required Args - arguments are the mandatory-
#args must be passed in correct number and order
def show(a,b):
    print(a+b)
show(10,20)


#Keyword args or Named Args - during the function call,
# keywords are mentioned  along with their corresponding values.
def empDetails(name,role):
    print(name,role)
empDetails(name="abhi",role="Dev")
empDetails(name="rahul",role="tester")


#Variable args- design where any number of arguments can be passed
def varlenargs(*argp):
    sum=0
    for i in argp:
        sum=sum+i
    print(sum)

varlenargs(10,20,30)



#'None' - special constant to represent absence of value or null value.
#'None' is not a 0 , false, []-
#Void functions that don’t return anything will return None object automatically
def add():
    a,b=10,20
    c=a+b
x=add() #output is none/null
#If the functions not returns the value but if we are trying to hold the
#values it return NONE as a default value. 

#Function return - no datatype is required
def add(x,y):
    return x+y
a,b = 10,20
Sum=add(a,b)
print(Sum)