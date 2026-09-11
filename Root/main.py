import random

choices = ["heads", "tails"]

while True:
    value = random.choice(choices)
    guess = input("What is your guess? Type 'quit' to end game\n")
    if guess == "quit":
        print("Thank you for playing!")
        break

    guess = guess.lower()
    if guess in choices:
        if guess == value:
            print("Correct!")
        else:
            print("Wrong!")
    else:
        print("Invalid answer")