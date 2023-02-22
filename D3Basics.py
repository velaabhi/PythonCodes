
#conversion of decimal to binary,octal, hex
d = 10
print(bin(d))
print(oct(d))
print(hex(d))

a,b,c,d = 0b10, 0o10,10, 0x10
print("a in bin=  ",a,", b in oct=  ",b,", c in dec=  ",c,",d in hex=  ",d)

hexa = 0x2ab
print(hexa)
octa = 0o0745
print(octa)
bina = 0b1100110
print(bina)     #in above 3 cases we get ans in decimal format

#finding ASCII values - ord()
c= input("Enter a character ")
print("ASCII value of character '"+c+"' is ", ord(c)) 


#convert integer to ASCII character  - chr()
print(chr(0xaa))
print(chr(0b110110))
print(chr(201))
print(chr(0o23))

print(chr(0))
print(chr(255))
#print(chr(-1))
print(chr(263))
for i in range (0,600):
    print(i ,"= ", chr(i))



#Basic datatype conversions
print("Float to int",int(123.223))
print("bool(T) to int",int(True))
print("Bool(F) to int",int(False))
print("Bool(F) to float",float(False))
print("Bool(F) to str",str(False))

a,b = 10,20
print("str+str",str(a)+str(b))
print("str to int ",int("10"))
print("str to float ",float("10.21"))
print("str to float",int("10.6"))


#flow control stmts 1
age = int(input("Enter age "))
if(age>=18):
    print("Vote")
else:
    print("Dont vote")


#flow control stmts 2
n1 = int(input("Enter 1st no "))
n2 = int(input("Enter 2nd no "))
if(n1>n2):
    print("n1 is greater")
else:
    print("n2 is greater")
   

#flow control stmts 3

if 0:
    print("hi amit")
else:
    print("hi anu")

if True:
    print("In IF block")
else:
    print("In Else block")


#1.if else - accept radius of 2 circles and find which is bigger circle by comapring area and by how much area
print("Code for comparing 2 circles based on areas")
r1=float(input("Enter r1 for circle1 "))
r2=float(input("Enter r2 for circle2 "))
a1=3.14*r1*r1
a2=3.14*r2*r2
if(a1>a2):
    a3=a1-a2
    print("Circle1 is greater than Circle2 by ",a3," area")
else:
    a3=a2-a1
    print("Circle2 is greater than Circle1 by ",a3," area")



#2.if else - accept a number from user and check if it is divisible by 4
print("Code for checking if number is divisible by 4")
n = int(input("Enter a no "))
if(n%4==0):
    print("Divisible")
else:    
    print("Not Divisible")
