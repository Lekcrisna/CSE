import random
import string
"""This is a guide of how to make hangman
1. Make a word bank - 10 items
2. Select a random item to guess
3. take in a letter and add it to a list of add_letters
4. Reveal letters based on input
5. Create a win and lose conditions
"""
guesses = 10

word_bank = ["Computer", "Science", "Burrito", "Laser",
             "Edison", "Triangle", "Blizzard", "Flapjack", "Jazz", "Perimeter"]

word = random.choice(word_bank)
letters_guessed = list(string.punctuation + " ")

output = []
while guesses > 0 and "".join(output) != word:
    output = []
    for letter in word:
        if letter.lower() in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print("".join(output))
    if "".join(output) == word:
        print("Good job")
        continue
    guess = input("Choose a Letter").lower()
    letters_guessed.append(guess)
    if guess not in word.lower():
        guesses -= 1
        print("You have %d guesses left" % guesses)