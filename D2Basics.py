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
"""

#Formatting data with % and {}
eid, ename, esal = 1,"Abhi", 100000.25
print("Emp id = %d, Emp Name = %s, Emp sal = %0.2f" %(eid,ename,esal)) 
print("Emp id : {}, Emp Name : {}, Emp sal : {}" .format(eid,ename,esal)) 
print("Emp id = {0}, Emp Name = {1}, Emp sal = {2}" .format(eid,ename, esal))#sequencing of format specifiers
print("Emp id = {1}, Emp Name = {2}, Emp sal = {0}" .format(eid,ename, esal)) 

