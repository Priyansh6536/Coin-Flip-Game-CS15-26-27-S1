import random


choices = ["heads", "tails"]
streak = 0
points = 10
while True:
    value = random.choice(choices)
    guess = input("What is your guess? Type 'quit' to end game\n")

    if guess == "quit":
        print("Thank you for playing!")
        break

    guess = guess.lower()
    if guess in choices:
        if streak < 5:
            if guess == value:
                print("Correct!")
                streak += 1
                points += 10
            else:
                print("Wrong!")
                streak = 0
                points = 0
            print("Streak :", streak)
            print("Points:", points)
        else:
            if guess == value:
                print("Correct!")
                streak += 1
                points += 20
            else:
                print("Wrong!")
                streak = 0
                points = 0
            print("Streak :", streak)
            print("Points:", points)
    else:
        print("Invalid answer")

