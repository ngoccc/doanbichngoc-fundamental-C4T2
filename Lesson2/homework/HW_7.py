# def fibo(a):
#     if (a == 0) | (a == 1) | (a == 2):
#         return a
#     else:
#         return fibo(a - 1) + fibo(a - 2)
#
#
# for i in range(0, 9):
#     if i == 1:
#         print(fibo(i), "1", end=" ")
#     elif (fibo(i) <= 50):
#         print(fibo(i), end=" ")

a = []
a.append(1)
a.append(1)
for i in range(2, 20):
    a.append(a[i - 1] + a[i - 2])
    if a[i] >= 50:
        a.remove(a[i])
        break
for i in a:
    print(i, end=" ")
