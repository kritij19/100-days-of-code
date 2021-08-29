
data = pd.read_csv(r'nato_phonetic_alphabet.csv')

# Dict with a letters as key and words as value

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

program_is_on = True

# Keep asking for input unless a valid input is entered.
while program_is_on:

    word =  input("Enter a word: ").upper()
    
    # Adding words from phonetic_dict whose key is same as letters in the name
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Only letters in the alphabets please!")
    else:
        print(output_list)
        program_is_on = False

