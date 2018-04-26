r = ["Yes", "yes", "y", "Y"]
attempt = 0
while True:
    response = input("Do you want to quit? (y/n): ")
    attempt += 1
    if response in r: break
print("Existing after ", attempt, "attempts")
