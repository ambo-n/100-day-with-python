import random
print("Welcome to the Number Guessing Game!")

continue_game=True

while continue_game:
    the_number = random.randint(1,100)
    print("I'm thinking of a number between 1 and 100")
    number_of_guesses=0
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        number_of_guesses=10
    elif difficulty == 'hard':
        number_of_guesses=5
    else:
        print("Invalid choice. Please type 'easy' or 'hard'.")
    while number_of_guesses > 0:
        print(f"You have {number_of_guesses} attempts remaining to guess the number")
        guess_number = int(input("Make a guess: "))
        if guess_number == the_number:
            print(f"You got it! The answer was {the_number} ")
            break
        elif guess_number < the_number:
            print("Too Low.")
            print("Guess Again")
            number_of_guesses -=1
        elif guess_number > the_number:
            print("Too High")
            print("Guess Again")
            number_of_guesses -=1
    if number_of_guesses ==0:
        print("Oops! You've run out of guesses.")
        print(f"The number was {the_number}")
    play_again =input("Would you like to play again? Type 'y' or 'n': ").lower()
    if play_again == 'n':
        print("Thanks for playing. Bye")
        continue_game=False

