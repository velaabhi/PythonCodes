"""

Complete the print_full_name function in the editor below.

print_full_name has the following parameters:

string first: the first name
string last: the last name
Prints

string: 'Hello firstname lastname ! You just delved into python' where firstname  and lastname are replaced with first and last.
"""

first =  input("Enter 1st name")
last = input("Enter last name")

res = 'Hello {} {} ! You just delved into python'.format(first,last)
print(res)