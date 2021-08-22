import random
import hangman_words as hw
import hangman_art as ha

word_list = hw.word_list
# Choosing a random word from a list of words in hangman_words.py

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# end_of_game is changed to true if either the number of lives become zero or the user has guessed the word
end_of_game = False
lives = 6
print(ha.logo)

#For testing
#print(f'Pssst, the solution is {chosen_word}.')

# Display contains blanks and fills letters when the user makes a correct guess
display = []
for i in range(word_length):
    display += "_"

while not end_of_game:
    # Guess stores the users guessed char
    guess = input("Guess a letter: ").lower()

    # If user has already entered the correct letter before
    if guess in display:
      print('You have already entered this letter. Make a new try')
    
    # Check guessed letter
    # Replace that location of display list with the guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    # The user loses a life if their guess is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word!")
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was {chosen_word}")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has won i.e. he has guessed all letterS i.e. no blanks in display.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Shows the hangman art corresponding to every stage. Art decided on the basis of the number of lives remaining.
    print(ha.stages[lives])
