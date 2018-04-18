# import math
#
# a = int(input("Nhap a: "))
# b = int(input("Nhap b: "))
# c = int(input("Nhap c: "))
# if a == 0:
#     print("Phuong trinh co 1 nghiem x = ", c / b)
# else:
#     delta = b ** 2 - 4 * a * c
#     if delta < 0:
#         print("Phuong trinh vo nghiem")
#     elif delta == 0:
#         print("Phuong trinh co nghiem duy nhat x = ", -b / (2 * a))
#     else:
#         x1 = (-b - (math.sqrt(delta))) / (2 * a)
#         x2 = (-b + (math.sqrt(delta))) / (2 * a)
#         print("Phuong trinh co 2 nghiem x1 = ", x1, " va x2 = ", x2)

# a = [1, 2, 3, 4]
# sum = 0
# for i in range(len(a)):
#     sum = sum + a[i]
# print(sum)

# import random
#
# a = []
# for i in range(20):
#     a.append(random.randint(0, 1000))
# print(a)
# max = a[1]
# for i in range(20):
#     if max < a[i]: max = a[i]
# print(max)

# a = [1, "xin chao", {2, 3}]
# b = [[1, 4], [2, 3, 4], 1]
# c = [{1, 2, 3, 4}, {8, 7, 9, 19}]
# for x, y, z, t in c:
#     print(x, y, z, t)

# a = [4, 6, 8, 9]
# print(a[2:4])

# a = ["sad", "happy"]
# n = '''░▄▀▄▀▀▀▀▄▀▄░░░░░░░░░
# ░█░░░░░░░░▀▄░░░░░░▄░
# █░░▀░░▀░░░░░▀▄▄░░█░█
# █░▄░█▀░▄░░░░░░░▀▀░░█
# █░░▀▀▀▀░░░░░░░░░░░░█
# █░░░░░░░░░░░░░░░░░░█
# █░░░░░░░░░░░░░░░░░░█
# ░█░░▄▄░░▄▄▄▄░░▄▄░░█░
# ░█░▄▀█░▄▀░░█░▄▀█░▄▀░
# ░░▀░░░▀░░░░░▀░░░▀░░░'''
# print(n)

# khai bao ham con
# import sub_function as sf
# b = [2, 5, 7]
# sum = sf.tinh_tong(b)
# print(sum)

print(ord("$"),ord("9"),ord("0"))
print(chr(92))