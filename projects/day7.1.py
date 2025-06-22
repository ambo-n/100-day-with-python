import random
word_list = ["aardvark","baboon","camel","kangaroo","koala"]
chosen_word = random.choice(word_list)
number_of_guesses =6
print(chosen_word)

placeholder =""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

display =""
guess=input("Guess a letter: ")
for letter in chosen_word:
    if letter ==guess:
        display+=letter
    else:
        display+="_"