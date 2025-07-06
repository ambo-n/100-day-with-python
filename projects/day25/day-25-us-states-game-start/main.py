import turtle
import pandas as pd
from guessboard import Guessboard

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

player_guesses =[]

guessboard = Guessboard()
data= pd.read_csv("50_states.csv")

game_is_on =True

while game_is_on:
    answer_state = screen.textinput(title=f"Guess the State. Correct guesses: {len(player_guesses)}/50", prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        break
    if answer_state in data.state.values and answer_state not in player_guesses:
        player_guesses.append(answer_state)
        state_data = data[data["state"] == answer_state]
        x_cor = int(state_data.x.values[0])
        y_cor = int(state_data.y.values[0])
        guessboard.update_guessboard(x_cor,y_cor, answer_state)
    if len(player_guesses) == 50:
        game_is_on = False
        guessboard.game_over()
        screen.exitonclick()

state_to_learn =[]
for state in data.state.values:
    if state not in player_guesses:
        state_to_learn.append(state)
new_data = pd.DataFrame(state_to_learn)
new_data.to_csv("state_to_learn.csv", index=False)