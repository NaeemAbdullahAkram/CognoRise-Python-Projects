import random

def choose_word():
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman_display(incorrect_guesses):
    stages = [
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / \
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / 
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |      
        """,
        """
           --------
           |      |
           |      O
           |     \|
           |      |
           |     
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
        """
    ]
    return stages[incorrect_guesses]

def main():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0

    print("Welcome to Hangman!")
    print(hangman_display(incorrect_guesses))
    print(display_word(word, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            incorrect_guesses += 1
            print("Incorrect guess!")
            print(hangman_display(incorrect_guesses))
        else:
            print("Correct guess!")

        displayed_word = display_word(word, guessed_letters)
        print(displayed_word)

        if "_" not in displayed_word:
            print("Congratulations! You guessed the word:", word)
            break

        if incorrect_guesses == len(hangman_display(0).split("\n")) - 1:
            print("Sorry, you've run out of guesses. The word was:", word)
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        main()

if __name__ == "__main__":
    main()