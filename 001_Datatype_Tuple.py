n = input("Enter n - ")
seq = list(map(int,input("Enter values sepearted by spaces - ").split()))

t1 = tuple(seq)
print(t1)
print(abs(hash(t1)))