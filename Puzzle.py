import random

words = ["python", "machine", "learning", "cloud", "vision"]  # List of words
word = random.choice(words)  # Randomly select a word from the list
attempts = 2

while attempts > 0:
    guess = input("Enter your guess: ").lower()
    if guess == word:
        print("Congratulations!!! Your guess is right.")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect! You have {attempts} attempts left.")
        else:
            print(f"Sorry, you have run out of attempts. The correct word was '{word}'.")

