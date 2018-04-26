import random

a = []
for i in range(10):
    a.append(random.randint(1, 50))
print(a)

even = 0
odd = 0
for i in a:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Number of even numbers: ", even)
print("Number of odd numbers: ", odd)
