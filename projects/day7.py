import random
word_list = ["scribe","baboon","camel","kangaroo","koala"]
hang_man_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

chosen_word = random.choice(word_list)
# print(chosen_word)
placeholder = "_"*len(chosen_word)
print(placeholder)
game_over = False
correct_letters=[]
number_of_lives =6
hang_man_progress=0
while not game_over:

    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f"You have already guessed {guess}")
    display=""

    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
        
    if guess not in chosen_word:
        number_of_lives -=1
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        hang_man_progress+=1
        if number_of_lives ==0:
            print("You lost!")
            game_over=True
            
    print(f"Word to guess: {display}")
    print(hang_man_pics[hang_man_progress])

    if "_" not in display:
        game_over=True
        print("You win!")
        
    

