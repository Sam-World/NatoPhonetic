import pandas


alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

# create a dictionary in the format {"A": "Alfa", "B": "Bravo"} from csv
nato_dict = {row.letter: row.code for (index, row) in alphabet.iterrows()}
# print(nato_dict) test

word = input("Choose a word: ").upper()

# create list of phonetic words from input
phonetic_list = [nato_dict[letter] for letter in word]
print(phonetic_list)
