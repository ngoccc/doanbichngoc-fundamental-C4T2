m = int(input("Rows = "))
n = int(input("Columns = "))
a = []
b = []
for i in range(m):
    for j in range(n):
        b.append(i * j)
    a.append(b)
    b = []
print(a)