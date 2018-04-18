s = input("Enter string: ")
letter = 0
digit = 0
for i in s:
    m = ord(i)
    if (m > 47) and (m < 58):
        digit += 1
    elif ((m > 64) and (m < 91)) or ((m > 96) and (m < 123)):
        letter += 1
print("Letters = ", letter)
print("Digits = ", digit)
