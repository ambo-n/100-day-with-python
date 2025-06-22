import random
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
if user_input == 0:
    print("You chose rock")
elif user_input == 1:
    print("You chose paper")
elif user_input==2:
    print("You chose scissors")
else:
    print("Invalid choice")

computer_input = random.randint(0,2)

if computer_input == 0:
    print("Computer chose rock")
elif computer_input == 1:
    print("Computer chose paper")
elif computer_input==2:
    print("Computer chose scissors")
else:
    print("Invalid choice")

if user_input == computer_input:
    print("It's a draw")
elif user_input == 0 and computer_input == 1:
    print("You lose")
elif user_input ==0  and computer_input == 2:
    print("You won")
elif user_input ==1 and computer_input==0:
    print("You won")
elif user_input==1 and computer_input == 2:
    print("You lost")
elif user_input==2 and computer_input==0:
    print("You lost")
elif user_input==2 and computer_input==1:
    print("You won")
else:
    print("Check your combo again")
