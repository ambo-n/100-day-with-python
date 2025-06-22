from data import data
import random

def famous_person_generator(data_list):
    """Randomly generate the famous person"""
    return random.choice(data_list)

def check_if_same_person(person_one, person_two):
    return person_one == person_two

def game_set_up():
    """Returns two distinct famous people"""
    person_a = famous_person_generator(data)
    person_b = famous_person_generator(data)
    while check_if_same_person(person_a, person_b):
        person_b = famous_person_generator(data)
    return person_a, person_b

def format_person(person,label):
    return f"{label}: {person['name']}, a {person['description']}, from {person['country']}"

def get_winner(person_a, person_b):
    return 'A' if person_a['follower_count'] > person_b['follower_count'] else 'B'

def play_game():
    current_score=0
    famous_person_a, famous_person_b = game_set_up()
    while True:
        print(format_person(famous_person_a, "Compare A"))
        print("VS")
        print(format_person(famous_person_b,"Against B"))
        choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        winner = get_winner(famous_person_a, famous_person_b)
        if choice == winner:
            current_score +=1
            print("\n" *3)
            print(f"You are right! Current score: {current_score}")
            famous_person_a = famous_person_b
            famous_person_b = famous_person_generator(data)
            while check_if_same_person(famous_person_a, famous_person_b):
                famous_person_b = famous_person_generator(data)
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}")
            break

def main():
    print("Welcome to Higher Lower! Game Rule: Guess who has more followers!")
    while True:
        play_game()
        again = input("Play again? Type 'y' or 'n': ").lower()
        if again !='y':
            print("Thanks for playing. Bye!")
            break
if __name__ == "__main__":
    main()