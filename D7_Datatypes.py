
#1.Boolean
print(bool(1))

print(bool(0))

print(bool(-5))

print(bool(True))

print(bool(False))

print(1==1)

print(5>3)

print(True or False)

print(3>7)

print(True and False)

print("ketan"=="ketan")

print('a'=="a")

print(1 == True)

print(0==False)

print(True+True)

print(False+False)


#string -slice notation [Start index: stop index]
str = "Ketanit"
print(str[3])
print(str[1:3])
print(str[1:4:2])
print(str[3:])
print(str[:4])
print(str[:])
#print(str[20])
print(str[-3])
print(str[-6:-4])
print(str[-3:])
print(str[:-5])
#print(str[-9])
print(str[-2:-4])

#len and strip()
n = " ketan "   #str with spaces
print(len(n))
print(n.strip())
print(len(n.strip()))

n2= "@@@ketan###"
print(n2.lstrip("@"))
print(n2.rstrip("#"))
print(n2.lstrip("@").rstrip("#"))


n3= "@@@ketan$###"
print(n3.rstrip("#").rstrip("$"))

















