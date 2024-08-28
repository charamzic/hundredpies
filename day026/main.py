import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row for index, row in data.iterrows()}

word = input("Enter a word: ").upper()
result = [phonetic_dict[letter] for letter in word]
print(result)
