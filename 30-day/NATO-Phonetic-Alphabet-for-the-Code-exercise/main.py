# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def stuff():
        word = input("Enter a word: ").upper()
        output_list = []
        try:
                for letter in word:
                        output_list.append(phonetic_dict[letter])
        except KeyError:
                print(f"Input should only contain letters, please retry")
                stuff()
        else:
                print(output_list)

stuff()