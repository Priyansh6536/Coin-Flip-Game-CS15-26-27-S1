import random


choices = ["heads", "tails"]
streak = [0]
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
            streak[0] += 1
        else:
            print("Wrong!")
            streak = [0]
        print("Streak :", streak)
    else:
        print("Invalid answer")

