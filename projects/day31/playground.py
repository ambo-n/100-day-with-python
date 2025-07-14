import pandas as pd
import random

data_file = pd.read_csv("flash-card-project-start/data/french_words.csv")
list_of_word = data_file.to_dict('records')
print(list_of_word)
chosen_word= random.choice(list_of_word)
print(chosen_word)
list_of_word.remove(chosen_word)
print(list_of_word)
french_word = chosen_word['French']
english_word = chosen_word['English']
