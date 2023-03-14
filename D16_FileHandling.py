"""
#1. Write Op
text = "hi ketan sir \n  Welcome to pune"
f = open ("sample.txt","w")
f.write(text)
f.close()
print("Ops completed ")

#2. Read op
f1 = open("sample.txt","r")
s = f1.read()
print(s)
"""

#3.seek funct
f = open("sample.txt","r")
s = f.read()
print(s)
f.seek(0)
s1 = f.read(2)
print(s1)

f.seek(5)
s2 = f.read(3)
print(s2)

print(f.tell())
f.close()












