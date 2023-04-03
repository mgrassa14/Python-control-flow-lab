# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant
# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

letter = input('Enter a letter from the alphabet: ').lower()
vowel = f"The letter {letter} is a vowel"
consonant = f"The letter {letter} is a consonant"

while letter != 'qq':
    for l in letter:
        if l == 'a':
            print(vowel)
        elif l == 'e':
            print(vowel)
        elif l == 'i':
            print(vowel)
        elif l == 'o':
            print(vowel)
        elif l == 'u':
            print(vowel)
        else:
            print(consonant)
        letter = input('Enter a letter from the alphabet: ').lower()
        vowel = f"The letter {letter} is a vowel"
        consonant = f"The letter {letter} is a consonant"

# my first idea before I saw the hint
# letter = input('Enter a letter from the alphabet: ').lower()
# while letter != 'qq':
#     if (letter == 'a') or (letter == 'e') or (letter == 'i') or (letter == 'o') or (letter == 'u'):
#         print('The letter is a vowel')
#     else:
#         print('The letter is a consonant')
#     letter = input('Enter a letter from the alphabet: ').lower()