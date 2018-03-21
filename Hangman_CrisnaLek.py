import random
"""This is a guide of how to make hangman

1. Make a word bank - 10 items
2. Select a random item to guess
3. take in a letter and add it to a list of add_letters
4. Reveal letters based on input
5. Create a win and lose conditions

"""
guesses = 10

word_bank = ("Computer", "science", "burrito", "laser",
             "Edison", "triangle", "blizzard", "flapjack", "jazz", "perimeter",)

random_letter = (random.choice(word_bank))
print(random_letter)
print("You have 10 guesses, whats the correct letter ?")
guessed = [0]

while guesses > 0:
    guess = -1
print(guesses)
print("Your letters, %s" % list2)
output = ['*']
for letter in random_letter:
    if letters_guessed:
        outpend.append(letter)
else:
    outpend.append("*")
print("".join(output))


if list(the_word) == output:
    print("You win")
    exit(0)

guess = input("type in a letter:")
