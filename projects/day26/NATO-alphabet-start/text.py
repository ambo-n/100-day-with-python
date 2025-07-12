import pandas as pd

nato_phonetic = pd.read_csv("nato_phonetic_alphabet.csv")

for index,row in nato_phonetic.iterrows():
    print(row.code)