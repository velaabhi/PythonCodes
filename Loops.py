#execute a block of code several nosof times.
'''
#while -  true is any non-zero value
cnt =0
while(cnt<9):
    print(cnt)
    cnt = cnt+1
print("Bye")

# for- used to iterate over any seq such as list,tuple,string etc

#for with list and 'in'
langs = ['C','Cpp','Java','Python']
for l in langs:             #using 'in' operator
    print(l)

#for with range()
val= range(4)       #range() to def range of vals between 0-3
for i  in val:
    print(i)

#for loop with else
digits = [1,4,7,8]
for j in digits:
    print(j)
else:
    print("No item left")

#break 
for i in range(1, 10):
    if(i==4):
        break
    print(i)
for letter in "ketan":
    if letter == 't' or letter == 'a':
        break
    print ('Current Letter :', letter)


#else bloack will not be executed if 1.exception occurs,2.break,3.os.exit()
#case1- exception occurs
for i in range(10):
    print("Magic",i)
   # print(10/0)
else:
    print("Exited with else")

#case2 -by break 
for i in range(8):
    print("Hi",i)
    if(i==4):
        break
else:
    print("else of for loop")

#else is always executed when while/for loop terminated normally.
'''

#Nested Loop  - prog to check prime nos in given range
lowerd = int(input("Enter lower range"))
upperd = int(input("enter higher range"))
print("Prime numbers between", lowerd, "and", upperd, "are:") 
for num in range(lowerd,upperd+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)

#Pass is an empty statement in python.If you want declare the func now w/t 
#implementation, but you want provide the implementation in future use pass statement. 