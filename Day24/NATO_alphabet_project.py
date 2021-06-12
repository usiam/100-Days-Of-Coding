import pandas
csvName = 'nato_phonetic_alphabet.csv'
letterCodeData = pandas.read_csv(csvName)
phoneticDict = {row.letter : row.code for (index, row) in letterCodeData.iterrows()}
word = input("Enter a word: ").upper().strip()
outList = [phoneticDict[letter] for letter in word]
print(outList)

