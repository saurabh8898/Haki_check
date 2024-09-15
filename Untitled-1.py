def guess_word():
    secret_word = "python"  # Replace with your desired secret word
    guessed_letters = []
    attempts = 5
    
    while attempts > 0:
        # Display current progress of guessed word
        display_word = "".join([letter if letter in guessed_letters else '_' for letter in secret_word])
        print(f"Word to guess: {display_word}")
        
        # Prompt user for a letter
        guess = input("Enter a letter: ").lower()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue
        
        # Add guessed letter to list
        guessed_letters.append(guess)
        
        # Check if the letter is in the secret word
        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts -= 1
        
        # Check if the word has been fully guessed
        if all(letter in guessed_letters for letter in secret_word):
            print(f"Congratulations! You guessed the word '{secret_word}' correctly.")
            break
    
    if attempts == 0:
        print(f"Out of attempts. The word was '{secret_word}'.")

# Run the game
guess_word()
