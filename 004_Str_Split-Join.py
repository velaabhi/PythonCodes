#You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.


s1 = input()
s2 = s1.strip()
res = s2.split(" ")
result = "-".join(res)
print(result)