import random
import hangman_words
import hangman_art

logo = hangman_art.logo
print(f"Welcome to hangman  {logo}")


word_list = hangman_words.word_list
lives = 6



chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    
    print(f"****************************{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

   
    if guess in correct_letters:
            print(f"You guessed the letter before'{guess}'")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"




    # for letter in correct_letters:
    #     if
    #     print(f"You guessed the letter before'{guess}'")
    print("Word to guess: " + display)

   
   

    if guess not in chosen_word:
        print(f"You guessed the wrong letter '{guess}' you lose a life" )
        lives -= 1

        if lives == 0:
            game_over = True

            
            print(f"***********************YOU LOSE******{chosen_word} is the word you were trying to guess" )

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")


    stages = hangman_art.stages
    print(stages[lives])
