import pandas as pd
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

nato_phonetic = pd.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic_dict = {row.letter:row.code for (index,row) in nato_phonetic.iterrows()}


while True:
    user_input = input('Enter a word: ').upper()
    if user_input == 'QUIT':
        break
    try:
        output = [nato_phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
    else:
        print(output)