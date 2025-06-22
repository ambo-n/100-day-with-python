import random

def get_valid_difficulty():
    while True:
        choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if choice =='easy':
            return 10
        elif choice=='hard':
            return 5
        print("Invalid choice. Try again")

def play_game():
    print("I'm thinking of a number between 1 and 100")
    number = random.randint(1,100)
    guesses = get_valid_difficulty()
    while guesses >0:
        print(f"You have {guesses} attempts remaining")
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number")
            continue
        if guess == number:
            print(f"You got it! The anser was {number}")
            return
        elif guess < number:
            print("Too low")
        else:
            print("Too high")
        guess -=1
        if guess > 0:
            print("Guess again")
    print(f"You have run out of guesses. The number was {number}.")

def main():
    print("Welcome to the Number Guessing Game!")
    while True:
        play_game()
        again = input("Play again? Type 'y' or 'n': ").lower()
        if again !='y':
            print("Thanks for playing. Bye!")
            break

main()