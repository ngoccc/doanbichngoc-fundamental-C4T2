# [1]
# for i in range(2000, 3200):
#     if i % 7 == 0 and i % 5 != 0:
#         print(i, end=", ")
#
# [2]
# n = int(input("Enter n: "))
# f = 1
# for i in range(1, n + 1):
#     f *= i
# print(f)
#
# [3]
# d = {}
# n = int(input("Enter n: "))
# for i in range(1, n + 1):
#     d[i] = i ** 2
# print(d)
#
# [4]
# a = [x for x in input("Nhap so: ").split(",")]
# l = []
# t = ()
# for i in a:
#     l.append(i)
# t = tuple(l)
# print(l)
# print(t)
#
# [5]
# s = input("Enter string: ")
# print(s.encode('utf-8'))
#
# [6]
# -*- coding: utf-8 -*-
# [7]
# n = int(input("Enter n: "))
# sum = 0
# for i in range(1, n + 1):
#     sum += i / (i + 1)
# print(sum)
#
# [8]
# print(abs.__doc__)
#
# [9]
# n = int(input("Enter n: "))
# if n%2==0: print("It is an even number")
# else: print("It is an odd number")
#
# [10]
# def TinhTong(n):
#     if n == 0:
#         return 1
#     else:
#         return TinhTong(n - 1) + 100
# a = int(input("Enter a: "))
# print(TinhTong(a))
#
# [11]
# a = [12, 24, 35, 24, 88, 120, 155]
# set = []
# for i in a:
#     if i not in set: set.append(i)
# print(set)
#
# []
# for rabbit in range(1, 35):
#     if (rabbit * 4 + (35 - rabbit) * 2) == 94:
#         print("Rabbits = ", rabbit)
#         print("Chicken =", 35 - rabbit)
#
# x = 10
# while x!=5:
#     x -= 1
#     if x % 2 != 0: continue
#     print(x, end=" ")
#
# lop_C4T = {"Tenlop": "C4T", "Siso": 15}
# print(lop_C4T.keys())
# print(lop_C4T.values())
# lop_C4T["Tenlop"] = "hello"
# print(lop_C4T["Siso"])

a = (1, 2, 3)
b = (1, 2)
print(hex(id(a)))
a = a + b
print(hex(id(a)))
print("array")
c = [1, 2, 3]
print(hex(id(c)))
c.append([1,2])
print(hex(id(c)))