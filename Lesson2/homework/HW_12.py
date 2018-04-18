def Check(a):
    uppercaseLetter = 0
    lowercaseLetter = 0
    number = 0
    char = 0
    if len(a) >= 6 and len(a) <= 16:
        for i in a:
            m = ord(i)
            if m >= 97 and m <= 122:
                lowercaseLetter += 1
            elif m >= 65 and m <= 90:
                uppercaseLetter += 1
            elif m >= 48 and m <= 57:
                number += 1
            elif m == 35 or m == 36 or m == 64:
                char += 1
    if lowercaseLetter >= 1 and uppercaseLetter >= 1 and char >= 1 and number >= 1: return True
    return False


password = input("Enter password: ")
if (Check(password) == True):
    print("Valid")
else:
    print("Invalid")
