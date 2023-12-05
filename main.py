"""
Morse code convert
String to Morse code
"""

import pandas as pd

# International Morse Code
data = pd.read_csv('Morse_Code.csv')
data.Character = data.Character.astype(str)

print('Morse Code Translator')

is_on = True


def morse_code_convert():
    for char in phrase:
        print(data.Code[data.Character == char].to_string(index=False), end=" ")


while is_on:
    phrase = input('Enter a word or phrase: ')
    phrase = list(phrase.upper())
    morse_code_convert()
    is_on = True if input('\n Do you want to continue?y/n: ').upper() == 'Y' else False
