
import random
list_of_cards= [11,2,3,4,5,6,7,8,9,10,10,10,10]

def card_calculator(player_card, dealer_card):
    player_card_sum=0
    dealer_card_sum=0
    player_aces=0
    dealer_aces=0
    for card in player_card:
        if card ==11:
            player_aces+=1
        player_card_sum += card
    for card in dealer_card:
        if card ==11:
            dealer_aces+=1
        dealer_card_sum+=card
    while player_card_sum >21 and player_aces:
        player_card_sum -=10
        player_aces -=1
    while dealer_card_sum >21 and dealer_aces:
        dealer_card_sum -=10
        dealer_aces -=1
    return player_card_sum, dealer_card_sum

def dealing_cards(input_list, output_list):
    output_list.append(random.choice(input_list))
    output_list.append(random.choice(input_list))

def dealer_draw(dealer_card, dealer_card_sum):
    while dealer_card_sum <17 and dealer_card_sum < 22:
        dealer_card.append(random.choice(list_of_cards))
        dealer_card_sum = sum(dealer_card)
    return dealer_card_sum
    
def get_another_card(player_card,dealer_card):
    while True:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        player_card_sum,dealer_card_sum = card_calculator(player_card,dealer_card)
        if another_card == 'y':
            player_card.append(random.choice(list_of_cards))
            player_card_sum,dealer_card_sum = card_calculator(player_card,dealer_card)
            print(f"Your cards: {player_card}, current score: {player_card_sum} ")
            print(f"Computer's first card: {dealer_card[0]}")
            if player_card_sum > 21:
                print(f"\tYour final hand {player_card}, final score: {player_card_sum}")
                print(f"\tComputer's final hand: {dealer_card}, final score: {dealer_card_sum}")
                print("\tYou went over. You lose 😢")
                return player_card_sum
        else:
            return player_card_sum


def determine_winner(player_card_sum, dealer_card_sum):
    if player_card_sum == dealer_card_sum:
        print("\tIt's a draw! 🤝")
        print(f"\tYour final hand {player_card}, final score: {player_card_sum}")
        print(f"\tComputer's final hand: {dealer_card}, final score: {dealer_card_sum}")
    elif player_card_sum > dealer_card_sum and player_card_sum <22:
        print("\tYou won! 💪")
        print(f"\tYour final hand {player_card}, final score: {player_card_sum}")
        print(f"\tComputer's final hand: {dealer_card}, final score: {dealer_card_sum}")
    elif player_card_sum < dealer_card_sum and dealer_card_sum <22:
        print("\tYou lose 😢")
        print(f"\tYour final hand {player_card}, final score: {player_card_sum}")
        print(f"\tComputer's final hand: {dealer_card}, final score: {dealer_card_sum}")
    else:
        print("Dealer went over. You won! 💪")
        print(f"\tYour final hand {player_card}, final score: {player_card_sum}")
        print(f"\tComputer's final hand: {dealer_card}, final score: {dealer_card_sum}")

continue_game = True
print("Welcome to my BlackJack game!")
while continue_game:
    player_card = []
    dealing_cards(list_of_cards,player_card)
    dealer_card=[]
    dealing_cards(list_of_cards,dealer_card)
    player_card_sum,dealer_card_sum = card_calculator(player_card,dealer_card)
    print(f"Your cards: {player_card}, current score: {player_card_sum} ")
    print(f"Computer's first card: {dealer_card[0]}")
    player_card_sum=get_another_card(player_card, dealer_card)
    if player_card_sum < 22:
        dealer_card_sum=dealer_draw(dealer_card,dealer_card_sum)
        determine_winner(player_card_sum, dealer_card_sum)
    continue_playing = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")
    if continue_playing == 'n':
        continue_game= False
        print("Thanks for playing. Goodbye")

