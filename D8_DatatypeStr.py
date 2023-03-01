
#1. String datatype and its functions
n1 = "Ketan"
n2 = "anu"
n3 = "Ketan"

print(id(n1))   #id returns mem address
print(id(n2))
print(id(n3))
                   #is and is not are operators 
print("check val of n1 n2",n1==n2)
print("check val of n1 n3",n1==n3)
print("check val of n1 not-eq n2",n1!=n2)
print("check val of n1 not-eq n2",n1!=n3)

print(n1 is n2)     # is checks mem address
print(n1 is n3)
print(n1 is not n2)
print(n1 is not n3)

                #in and not in are operators while count is a function
s1="Ketanit"    
print("Ketan" in s1)        # in operator is used to check presence of str/char in str
print("durga" in s1)
print("Ketan" not in s1)
print("durga" not in s1)

s2 = "KetanKetan"
print(s2.count('a'))        #count returnsno of data occurances
print(s2.count('Ketan'))
print(s2.count('a',2,7))
print(s2.count('Ketan',2,7))


#2. str formatting with % operator
x,y = "Apples","lemon"
a,b = 10,10.5
print("In the basket are %s%d and %s%f" %(x,a,y,b))

#3. str formatting with { } operator
eid,ename,esal = 111,"Ketan", 1012.32
print("Emip id = %d Emp name= %s Emp sal = %g"%(eid,ename,esal))
print("Emip id = {} Emp name= {} Emp sal = {}".format(eid,ename,esal))
print("Emip id = {0} Emp name= {1} Emp sal = {2}".format(eid,ename,esal))


#4. Concat (+ operator) and Replication(* Operator)
s1= "Ketan"
s2="anu"
s3=s1+s2 #concat
print(s3)

s1= "Ketan"
s2="anu"
s3 = s1*3  #repitition
print(s3)



#5. string comparison
s1= "Ketan"
s2="anu"
print("s1 = ",s1,"and s2 = ",s2)
print("s1>s2",s1>s2)
print("s1<s2",s1<s2)
print("s1>=s2",s1>=s2)
print("s1<=s2",s1<=s2)
print("s1==s2",s1==s2)
print("s1!=s2",s1!=s2)
'

#6. string methods
s="Welcome all guys to Python Session"
print("find ",s.find("l"))  #returns 1st instance, -1 if absent
print("rfind ",s.rfind("l"))    #returns last instance, -1 if absent
print("index ",s.index("o"))    #returns 1st instance, value error if absent
print("rindex ",s.rindex("o"))  # returns last instance, value error if absent

print("split ",s.split("l"))        #slipts the str based on the char passed
s1 = "  "+s+"  "
print(s1)
print("strip ",s1.strip())      #strips leading and trailing white spaces

print("splitlines  ",s.splitlines())   #splits str into a list of str, 1 per line
print("lower  ",s.lower())      #convert to lower case
print("upper  ",s.upper())      #convert to upper case
print("title  ",s.title())      #title cased version
print("capitalize  ",s.capitalize())    
print("text join  ","*".join(s))
print("replae ",s.replace("a","T"))

print("starts with Welcome  ",s.startswith("Welcome"))
print("starts with  come 3,10 ",s.startswith("come",3,10))
print("ends with Session  ",s.endswith("Session"))
print("ends with  to 2,16 ",s.endswith("to",2,16))


#7. is related methods
s1="Python310"
print(s1, "isalnum ",s1.isalnum())   #ret T if str has alpha and num, else F

s1="Python"
print(s1, "isalpha ",s1.isalpha())   #ret T if str has alpha, else F

s1="310"
print(s1, "isdigit ",s1.isdigit())   #ret T if str  num, else F

s1="python"
print(s1, "islower ",s1.islower())   #ret T if str all aplha is lower, else F

s1="PythonHii"
print(s1, "isupper ",s1.isupper())   #ret T if str all aplha is upper, else F

s1="  "
print(s1, "isspace ",s1.isspace())   #ret T if str all char are whitespaces, else F


#8.enumerate funct - contains tuple of index and value of chars of a str
s = "Ketanit"
print(tuple(enumerate(s)))  #create tuple of above tuples
print(list(enumerate(s)))  #create list of above tuples





