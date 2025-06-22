import random

deck=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def calculate_hand_total(cards):
    total = sum(cards)
    aces = cards.count(11)
    while total >21 and aces:
        total -=10
        aces -=1
    return total

def deal_initial_cards():
    return [random.choice(deck), random.choice(deck)]

def dealer_draw_until_minimum(dealer_cards):
    while calculate_hand_total(dealer_cards) <17:
        dealer_cards.append(random.choice(deck))
    return calculate_hand_total(dealer_cards)

def player_draw_phase(player_cards, dealer_cards):
    while True:
        player_total = calculate_hand_total(player_cards)
        dealer_total =calculate_hand_total(dealer_cards)
        print(f"Your cards: {player_cards}, current score: {player_total} ")
        print(f"Computer's first card: {dealer_cards[0]}")
        if player_total >21:
                print(f"\tYour final hand {player_cards}, final score: {player_total}")
                print(f"\tComputer's final hand: {dealer_cards}, final score: {dealer_total}")
                print("\tYou went over. You lose 😢")
                return player_total
        choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if choice == 'y':
             player_cards.append(random.choice(deck))
        else:
             return player_total

def determine_winner(player_cards, dealer_cards):
    player_total = calculate_hand_total(player_cards)
    dealer_total = calculate_hand_total(dealer_cards)
    print(f"\tYour final hand: {player_cards}, final score: {player_total}")
    print(f"\tComputer's final hand: {dealer_cards}, final score: {dealer_total}")

    if player_total > 21:
        print("\tYou went over. You lose 😢")
    elif dealer_total > 21:
        print("\tDealer went over. You win! 💪")
    elif player_total == dealer_total:
        print("\tIt's a draw! 🤝")
    elif player_total > dealer_total:
        print("\tYou win! 💪")
    else:
        print("\tYou lose 😢")

def play_blackjack():
    print("Welcome to my Blackjack game!")
    while True:
        player_cards = deal_initial_cards()
        dealer_cards = deal_initial_cards()
        player_total = player_draw_phase(player_cards, dealer_cards)
        if player_total <= 21:
            dealer_total = dealer_draw_until_minimum(dealer_cards)
            determine_winner(player_cards, dealer_cards)
        again = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")
        if again == 'n':
            print("Thanks for playing. GoodBye!")
            break
        else:
            print("\n*20")
    
play_blackjack()