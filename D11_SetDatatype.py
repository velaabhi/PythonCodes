"""
#1. Set
s={1,2,3}
print(s)
print(type(s))

s1 = {10.2,"Hiii",(1,2,3)}
print(s1)

s3={1,1,1,2,3,4}
print(s3)       #duplicates not allowed
print(len(s3))

s4={}
print(type(s4)) #type is dict
s5=set()
print(type(s5))  #type is set

#2.set is mutable
s6={1,2,3}
s6.update([4,5],{1,6,8})
print(s6)


s1 = {1,2,3}
a = s1.copy()
print(a)

s2 = {1,2,3}
s2.add(4)
print(s2)

s2.discard(2)
print(s2)
s2.remove(8)
print(s2)


#3. pop,clear
s3={1,1,1,2,3,4}    #pop()
print("\n",s3)
s3.pop()
print(s3)
s3.clear()
print(s3)


#4. for loop
s={"apple","banana"}
for fruit in s:
    print(fruit)

for l in set("apple"):
    print(l)


#5.  adding grp of vals in set

x = {i for i in range(10,20)}
print(type(x))
print(x)

x = {i*i for i in range(10,20)}
print(type(x))
print(x)

x = {i for i in range(10,20,2)}
print(type(x))
print(x)

l1 = [10,20,30,40,50]
s= set()
for x in l1:
    if(x>30):
        s.add(x)
print(s)

#6. unique value list by using set
l1 = ['ratan','anu','durga']
l2 = ['Jack','Sam','Susan']
l3= ['Jane','Jack','Susan']

engg = set(l1+l2+l3)    #here lists are concat hence allowed
print(engg)

#7. superset and subset     - returns bool
A = {'d',6,'y'}
B = {5,'a',6,'r','d','y'}
print(A.issubset(B))
print(B.issuperset(A))


"""
#8. Operators- set diff,union,intersection,symmetric
b1 = {'orange','apple','pear','banana'}
b2 = {'orange','kiwi','pear','banana'}

print(b1-b2)    #set diff   - obj in b1 but not in b2 

print(b1 | b2)  #set union - ORing

print(b1 & b2)  #set intersection - ANDing

print(b1 ^ b2)  #symmetric diff - uncommon objs

result= b1.difference_update(b2)
print(result)
print(b1)

















