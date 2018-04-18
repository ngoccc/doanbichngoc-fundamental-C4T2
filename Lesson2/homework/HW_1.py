n = int(input("Enter n: "))  # (em lam dang tong quat luon a)
for i in range(n * 2):
    if (i <= n):
        for j in range(i): print("*", end=" ")
        print()
    else:
        for j in range(n * 2 - i): print("*", end=" ")
        print()
