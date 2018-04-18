attempt = 0
while True:
    response = input("Do you want to quit? (y/n): ")
    attempt += 1
    if response == "Yes": break
print("Existing after ", attempt, "attempts")
