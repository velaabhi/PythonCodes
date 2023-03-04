
#1. extracting data from tuple
t1 = (10,20,30,40,50)
t2 = tuple()    #constructor

print("Type ",type(t2))
print("t1 is ",t1)
print("t1[0] is ",t1[0])
print("t1[2:4] is ",t1[2:4])
print("t1[1:4:2] is ",t1[1:4:2])
print("t1[:4] is ",t1[:4])
print("t1[2:] is ",t1[2:])
print("t1[:] is ",t1[:])
print("t1[::2] is ",t1[::2])
print("t1[2:10] is ",t1[2:10])
#print("t1[10] is ",t1[10])
print("t1[-3] is ",t1[-3])
print("t1[-4:-2] is ",t1[-4:-2])
print("t1[:-3] is ",t1[:-3])
print("t1[-3:] is ",t1[-3:])

t3= (10,20,30)
a,b = t3[0:2]  #if u want to extract all the elements without specifying indexes, make sure
                #that LHS of all variables matches the size of tuple

                #if less no of variables are there in LHS, then specify the indexing to tuple
                # on RHS 
print(a,b)


#2. nested tuple and unpacking
t = ((10,20),(30,40,50))
print(t[0])
print(t[1])
print(t[1][1])
print(t[0][1])
a,b = t #unpacking
print(type(a))
print(b)


t1 = (10,20,30)
for x in t1[1:1]:
    print(x)



#3. adding multiple data into tuple
t1 = tuple(x for x in range(10))
print(t1)

t2 = tuple(x+267 for x in range(10,26))
print(t2)

t3 = tuple(x*89 for x in range(10,99,4))
print(t3)

# t3[2]=0
# print(t3)

t1 = (10,20,30)
for x in t1[1:1]:
    print(x)


#4. concat and replication
t1 = (10,20,30)
t2 = (40,50,60)
t3 = t1+t2

print(t3)
print(t1)
print(id(t1))

t4 = t1*3
print(t4)   #replication

print(id(t1))
t1=t1+t2
print(id(t1))   #old ref vari points to new mem, so old obj remains w/o ref and hence gets destroyed
            #so addr of prev t1 and this t1 is different



#5. Coversion process to make tuple modifyable
t = (10,20,30)  #tuple
l  =list (t)        #convert it to list for performing modification
l.append(40)
l.insert(2,66)
print(l)

t1 = tuple(l)       #again re-convert
print(t1)

t2= ('a','b','h','i')
str1 = '+'.join(t2)
str2 = ''.join(t2) 
print(str1)
print(str2)



#6. appending data in tuple - use list
t1 = ("hi",5,[],True)
t1[2].append(100)
print(t1)



#7. count(), index() and len() funct
t1 = (10,20,10,10,30,40)
print(t1.count(10))
print(t1.index(20))
print(len(t1))
print(t1.index(10,2))

print(t1.index(10,2,4))

#8. min  and max - use homogenous data only
t1 = (10,20,30,40)
print(min(t1))
print(max(t1))

#9. sorting - for homogen objs
t1 = (53,21,30,40)

print(sorted(t1))
print(sorted(t1,reverse=True))









