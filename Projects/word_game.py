
import random

print(" Welcome to the Guessing Game!")
print("Select Difficulty Level:")
print("1. Easy   (1–20)")
print("2. Medium (1–50)")
print("3. Hard   (1–100)")

choice = int(input("Enter choice (1/2/3): "))

if choice == 1:
    low, high = 1, 20
elif choice == 2:
    low, high = 1, 50
elif choice == 3:
    low, high = 1, 100
else:
    print(" Invalid choice! Defaulting to Easy.")
    low, high = 1, 20

secret = random.randint(low, high)
tries = 0
max_tries = 5

print(f"\nGuess the number between {low} and {high}. You have {max_tries} tries.\n")

while tries < max_tries:
    guess = int(input("Your guess: "))
    tries += 1

    if guess == secret:
        print(f" Correct! You guessed it in {tries} tries.")
        break
    elif abs(secret - guess) <= 10:
        print(" Too close!")
    else:
        print(" Too far!")

if guess != secret:
    print(f" You lost! The number was {secret}.")





