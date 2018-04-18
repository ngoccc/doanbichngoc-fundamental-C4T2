# [5]
# [6]
# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# a = []
# for i in range(x):
#     b = []
#     for j in range(y):
#         b.append(i*j)
#     a.append(b)
# print(a)
#
# [7]
# s = input("Enter words: ")
# y = s.split(",")
# y = sorted(y)
# print(",".join(y))
# a = [7, 3, 5, 10]
# for i in range(len(a) - 1):
#     if a[i + 1] < a[i]:
#         tg = a[i + 1]
#         a[i + 1] = a[i]
#         a[i] = tg
# print(a)

# a = [x for x in input("").split(",")]
# # d = {}
# b = []
# n = 0
# # for i in a:
# #     d[i] = ord(i[0])
# #     n += 1
# for i in a:
#     b.append(ord(i[0]))
#     n += 1
# for i in range(len(b) - 1):
#     if b[i + 1] < b[i]:
#         tg = b[i + 1]
#         b[i + 1] = b[i]
#         b[i] = tg
# c = []
# for i in b:
#     for j in a:
#         if i == ord(j[0]): c.append(j)
# print(c)

# for i in range(n):
#     if d.values[i + 1] < d.values[i]:
#         tg = d.values[i + 1]
#         d.values[i + 1] = d.values[i]
#         d.values[i] = tg
# print(d)
#
# [8]
# s = input("")
# print(s.upper())
#
# [9]
# import
# s = input("Enter string: ")
# letter = 0
# digit = 0
# for i in s:
#     if i.isdigit() == True:
#         digit += 1
#     elif i.islower() == True or i.isupper() == True:
#         letter += 1
# print("Letters = ", letter)
# print("Digits = ", digit)
#
# [10]
# s = input("Enter string: ")
# uppercase = 0
# lowercase = 0
# for i in s:
#     if i.isupper() == True:
#         uppercase += 1
#     elif i.islower() == True:
#         lowercase += 1
# print("Letters = ", uppercase)
# print("Digits = ", lowercase)
#

# [11]
# t = [('Tom', '19', '80'), ('John', 20, 90), ('Jony', '17', '91'), ('Jony', '16', '93'), ('Json', '21', '85')]
# a = []
#
# # def sx(x1, x2):
# #     if x1 < x2:
# #         tg = x1
# #         x1 = x2
# #         x2 = tg
#
# for i in range(4):
#     if t[i + 1][0] < t[i][0]:
#         tg = t[i + 1]
#         t[i + 1] = t[i]
#         t[i] = tg
#
# for i in range(4):
#     if t[i][0] == t[i + 1][0]:
#         if int(t[i + 1][1]) < int(t[i][1]):
#             tg = t[i + 1]
#             t[i + 1] = t[i]
#             t[i] = tg
#
# for i in range(4):
#     if t[i][0] == t[i + 1][0] and int(t[i][1]) == int(t[i + 1][1]):
#         if int(t[i + 1][2]) < int(t[i][2]):
#             tg = t[i + 1]
#             t[i + 1] = t[i]
#             t[i] = tg
# print(t)


# [?]
# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)
#
# print(fibo(6))
#
# []
# a = ["I", "You"]
# b = ["Play", "Love"]
# c = ["Hockey", "Football"]
# for i in a:
#     for j in b:
#         for k in c:
#             print(i, j, k)
#
# []
# l = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
# a = set(l)
# print(a)
for i in range(2): print(i)