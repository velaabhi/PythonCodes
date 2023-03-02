
#1. count no of 'a' occured in str w/o count funct
s="aap aye bahar aye"
count=0
for i in s:
    if i == "a":
       count= count +1

print(count)

#2. count no of 'Ketan' occured in str w/o count funct
s="Ketan is brilliant boy. Ketan is playing cards"
count=0
print(s.split())
for i in s.split():
    if i=="Ketan" :
        count = count+1
print(count)
