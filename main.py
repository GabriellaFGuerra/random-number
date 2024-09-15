import random
while True:
    random_number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    print("Select a difficulty level:")
    print("1. Easy (10 guesses)")
    print("2. Medium (7 guesses)")
    print("3. Hard (5 guesses)")
    level = int(input())
    guesses = 10 if level == 1 else 7 if level == 2 else 5

    print("You have", guesses, "guesses.")

    for i in range(guesses):
        guess = int(input("Enter your guess: "))
        if guess == random_number:
            print("Congratulations! You guessed it! It took you ", i + 1, "guesses.")
            break
        elif guess < random_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
    else:
        print("Sorry, you ran out of guesses. The number was", random_number)
        
    print("Do you want to play again? (y/n)")
    if input().lower() != "y":
        break