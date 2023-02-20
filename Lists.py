list = [1,"abhi",95.89] #list ele enclosed in Sq Br, sep by comma, diff datatypes supp
tinylist = [2,"lax"]
print(list)
print(tinylist)

print(list[0])
print(list[1:3])   #prints element on indx 1,2... 3 is exluded 
print(tinylist*2)   # * for repetition
print(list+tinylist)    # + for concat
print (list[1] + tinylist[1])

list[2] = 'vela'   #list is mutable
print(list)   