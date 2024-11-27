import random

def hangman():
    # List of words to choose from
    words = ['python', 'hangman', 'programming', 'developer', 'function', 'variable', 'conditional', 'loop', 'exception']
    
    # Select a random word
    word_to_guess = random.choice(words)
    guessed_word = ['_'] * len(word_to_guess)  # Create a list of underscores for the guessed word
    guessed_letters = set()  # Set to store guessed letters
    max_attempts = 6  # Maximum number of incorrect guesses
    attempts = 0  # Counter for incorrect guesses

    print("Welcome to Hangman!")
    
    while attempts < max_attempts and '_' in guessed_word:
        print("\nCurrent word: " + ' '.join(guessed_word))
        print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")
        print(f"Remaining attempts: {max_attempts - attempts}")

        # Get user input
        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        # Add the guessed letter to the set of guessed letters
        guessed_letters.add(guess)

        # Check if the guessed letter is in the word
        if guess in word_to_guess:
            print(f"Good guess! '{guess}' is in the word.")
            # Update the guessed word
            for index, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts += 1

    # Game over conditions
    if '_' not in guessed_word:
        print("\nCongratulations! You've guessed the word: " + word_to_guess)
    else:
        print("\nGame over! The word was: " + word_to_guess)

# Run the game
if __name__ == "__main__":
    hangman()