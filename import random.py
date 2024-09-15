import random

def game():
    # Welcome message and instructions
    print("Welcome to the Guessing Game!")
    print("Guess any number between 1 and 100")

    # Choose difficulty level
    difficulty = input("Choose Difficulty: Easy or Hard:\n").lower()

    # Set attempts based on chosen difficulty
    if difficulty == "hard":
        attempts = 5
        print(f"You have {attempts} attempts.")
    elif difficulty == "easy":
        attempts = 10
        print(f"You have {attempts} attempts.")
    else:
        print("Invalid response. Please restart the game and choose either Easy or Hard.")
        return

    # Computer chooses a number between 1 and 100 randomly
    computer_guess = random.randint(1, 100)
    print (computer_guess)

    # Loop until the user runs out of attempts or guesses correctly
    while attempts > 0:
        guess = int(input("Choose a number: "))

        if guess == computer_guess:
            print("Congratulations! You guessed the correct number!")
            break
        elif guess > computer_guess:
            attempts -= 1
            print(f"Too high. You have {attempts} attempts left.")
        elif guess < computer_guess:
            attempts -= 1
            print(f"Too low. You have {attempts} attempts left.")

        if attempts == 0:
            print(f"Sorry, you've run out of attempts. The correct number was {computer_guess}.")

    # Ask if the user wants to play again
    go_again = input("Do you want to play again? yes or no: ").lower()
    if go_again == "yes":
        game()
    else:
        print("Thank you for playing!")

# Start the game for the first time
game()
