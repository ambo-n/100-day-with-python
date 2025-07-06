import pandas as pd

data= pd.read_csv("50_states.csv")
user_input=input("Guess a state ").title()

state_data = data[data["state"] == user_input]

x_cor = int(state_data.x.values[0])
print(x_cor)
