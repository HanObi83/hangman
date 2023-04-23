# Hangman Game

import random, os, time
from hangman_words import word_list
from hangman_art import logo, stages

def hangman():

    # Variables
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    letters_guessed = []
    end_of_game = False
    lives = 6
    guess_count = 0
    game_message = ""

    # Functions
    def game_board():
        print(f"{logo}\n")
        print(game_message)
        print("\n\n" + stages[lives])

    def play_again():
        again = input("\nWould you like to play again? ('y' or 'n') ").lower()
        if again == "y":
            hangman()
        else:
            print("\nOkay, Goodbye!")

    # Create display
    display = []
    for _ in range(word_length):
        display += "_"

    # Testing code
    print(f"Pssst, the solution is {chosen_word}.")

    # Start game
    while not end_of_game:
        # Game logo, game message, and hangman art.
        game_board()
        # Word display, letters guessed, and current guess.
        print(f"{' '.join(display)}")
        print("\nLetters guessed: " + " ".join(set(letters_guessed)))
        guess = input("\nGuess a letter: ").lower()
        
        # If letter guessed has already been guessed.
        if guess in letters_guessed:
            game_message = f"You've already, guessed the letter: {guess}"
        # If letter guessed hasn't been guessed.
        elif guess not in letters_guessed:
            guess_count += 1
            letters_guessed.append(guess)
            # Check if letter guessed is in word.
            # If so update word display.
            for position in range(word_length):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter
            # If letter guessed is not in word.        
            if guess not in chosen_word:
                lives -= 1
                game_message = f'Sorry, the letter "{guess}" is not in the word.'
                
        # Clear screen, and check if user has won/lost.
        os.system("cls")
        if "_" not in display:
            end_of_game = True
            game_message = (f"\nYou won! You guesseed the word, {chosen_word.upper()},"
                            f" in {guess_count} guesses.\n")
            game_board()
            time.sleep(3)
            play_again()
        elif lives == 0:
            end_of_game = True
            game_message = (f"\nYou lost. The word was: {chosen_word.upper()}.\n")
            game_board()
            time.sleep(3)
            play_again()

hangman()