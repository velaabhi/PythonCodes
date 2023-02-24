#1.break
for i in range (1,10):
    if(i==4):
        break
    print(i)

#2.break
for l in "ketan":
    if l == "t" or l=="a":
        break
    print("curr letter is ",l)
    

#3. continue
for i in range(1,10):
    if i==4:
        continue        #skips current iteration
    print(i)
    
#4.Conti
for l in "ketan":
    if (l=="t" or l=="a"):
        continue
    print(l)

#5.Else block in for
for i in range (1,10):
    print(i)
else:
    print("for completed successfully and now executing else")
print("done")


#6.Else block not exe in for when 1.exception is raised
for i in range(1,10):
    print("Hii",i)
    print(10/0)
else:
    print("Else block")


#7.Else block not exe in for when 2.break or continue is used inside a for
for i in range(10):
    print("pratap",i)
    if(i==4):
        break
else:
    print("Else block")
print("done")


#8.Else block not exe in for when 3.using exit(0)
import os
for x in range(6):
    print("Ganga",x)
    os._exit(0)
else:
    print("Else block")



#9.Else block with while
a=1 #initialisation
while(a<=10):
    print("Hwllo",a)
    a=a+1
else:
    print("Else block")
print("Done")


#10.Else block not exe in while when 1.exception is raised
a=1 #initialisation
while(a<=10):
    print("Hwllo",a)
    a=10/0
else:
    print("Else block")
print("Done")


#11.Else block not exe in while when 2.berak or continue occurs

while i in range(0,10): #since in range is an iterator and not a condition we cannot use it in while as while needs a condition
    if (i==4):
        break
    print("Amit",i)
    i++
else:
    print("Else block")
print("Done")

#!2.Else block not exe in for when 3.using exit(0)
import os
a=1
while(a<10):
    print("ketan it")
    os._exit(0)
    a+=1
else:
    print("else block")


#13. Prime no in a range by using nested for loops
lower = int(input("Enter lower no"))
upper = int(input("Enter upper no"))
print("prime no bet",lower," and ",upper," are ")
for num in range(lower,upper+1):
    if num>1:       #cz prime nos are grtr than 1
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)
            
