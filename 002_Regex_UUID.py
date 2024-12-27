'''
create a UUID for employes by following the rules given below
It must contain at least 2 uppercase English alphabet characters. -done
It must contain at least 3 digits (0 - 9).  -done
It should only contain alphanumeric characters (a-z, A-Z & 0-9). -done
No character should repeat.-done
There must be exactly 10 characters in a valid UID. -done
'''

T1 = int(input("Enter a no - "))
seq = []
for i in range(T1):
    seq.append(input("Enter UUI"))

for s1 in seq:
#    s1 = input("Enter a UUID")
#    s1 = "B9CD102354"
    set1 = set(s1)
    len(set1)

    upperCount = 0
    digitCount = 0

    if len(set1) == 10:
        for char in s1:

            if char.isalnum():

                if char.upper():
                    upperCount = upperCount+1

                if char.isdigit():
                    digitCount = digitCount+1

        if upperCount>=2 and digitCount>=3:
            print("Valid")

        else:
            print("Invalid")


    else:
        print("Invalid")