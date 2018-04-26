import random
n = random.randint(1,9)
guess = int(input("Guess a number: "))
while (n != guess):
    guess = int(input("Guess another number: "))
print("Well guessed!")