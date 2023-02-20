#hash-table type, has key value pair
#enclosed by curly braces ({ }) 
# values can be assigned and accessed using square braces ([])
#elements are unordered

dict = {}
dict[1] = "This is one" #[1] is key and "This is one" is value
dict[2] = "This is two"

print(dict)

tinydict = {'nam':'abhi', 'mail':'velaabhi'}    #key and val sep by COLON 
                                                # key-val pair sep by comma
print(tinydict)
print("Keys of tinydict are  ",tinydict.keys()) # tinydict.keys() for displaying keys
print("Vals of tinydict are  ",tinydict.values()) # tinydict.keys() for displaying keys

print(dict[1])