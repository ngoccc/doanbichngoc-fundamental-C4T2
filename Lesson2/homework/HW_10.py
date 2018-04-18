# ko hiu lam huhu
s = input("Enter sequence: ")
a = []
for i in range(0, len(s)):
    if i % 5 == 0:
        s1 = s[i] + s[i + 1] + s[i + 2] + s[i + 3]
        n = int(s1, base=2)
        if n % 5 == 0: a.append(s1)
for i in a:
    print(i, end=" ")
