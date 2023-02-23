"""
#1. Control Flow Stmts
a = int(input("Enter a no "))
if a==10:
    print("Pratap")
elif a==20:
    print("Anu")
elif a==30:
    print("Durga")
else:
    print("Kavya")


#2. Control Flow Stmts- Even/odd/+ve/-ve
x = int(input("Enter a no "))
if x<0:
    print("x is -ve ")
elif x%2==0:
    print("Val is +ve and even")
else:
    print("Val is +ve and odd")
print("Process completed")


#3. print appropr. msg if no is +ve
x=int(input("Enter a no "))
if x>0:
    print("No is Positive")
else:
    print("Enter a positive no")



#4. give 10% discouont if bill exceeds 1000
bill = int(input("Enter the bill amount "))
if bill>1000:
    dis = bill*.10
    print("Final amt to be paid is ",(bill-dis))
else:
    print("Please pay the bill of amt ",bill)

#5. check if leap yr or not
yr = int(input("Enter the yr "))
if ((yr%4==0) and ((yr%100==0) or (yr%400==0))):
    print("Yr is leap yr")
else:
    print("Yr not a leap yr ")


#6.Loops- accept no, do sum until user enters -ve or 0
a = int(input("Enter a no "))
sum=0
while(a>0):
    sum+=a
    a = int(input("Enter a no "))
print("Sum is \n",sum)
print("process completed")


#7.GCD of 2 nos
a=int(input("Enter 1st no "))
b=int(input("Enter 2nd no "))
while(a != b):
    if(a>b):
        a-=b
    else:
        b-=a
print("GCD is ",a)


#8. count no of digits and perform sum of those digits
n = int(input("Enter a no "))
dig = 0
sum=0
while(n!=0):
    r= n%10     #mod to get remainder 
    sum=sum+r
    n = n//10   #floor div to get Quo
    print("n = ",n)
    dig +=1     #increment
print("no of Digits is ",dig)
print("Sum of Digits is ",sum)


#9.tk in as upperlimit and lowerlimit from user and print sqr of values
lower = int(input("Enter lower limit "))
upper = int(input("Enter upper lim"))
for i in range (lower, upper+1,1):   #(upper+1) is taken cz we have to print sqr of last no also
    print("Sqr of no ",i," is ",i*i)


#10. Prime no
n=int(input("Enter a no "))
flag = True
for i in range(2,n):
    if n%i==0:
        flag=False
print("Prime "if flag==True else "Not Prime")

#11. Factorial
n=int(input("Enter a no "))
for i in range(1,n):
    n*=i
print("Factorial is ",n)

"""

#12. Fibonacci series
n=int(input("Enter a number"))
n1=0
n2=1

print("0\n1")
for i in range(0,n+1):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
