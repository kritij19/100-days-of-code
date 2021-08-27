
import pandas as pd

#TODO 1. Create a dictionary of {letter: word} from csv:

data = pd.read_csv(r'NATO-alphabet-start\nato_phonetic_alphabet.csv')

# Dict with a letters as key and words as value
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
# Adding words from phonetic_dict whose key is same as letters in the name
output_list = [phonetic_dict[letter] for letter in word]

print(output_list)
