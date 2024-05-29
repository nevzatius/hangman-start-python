#Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

display = []

for letter in chosen_word:
  display += "_"
print(display)

guess = input("Guess a letter:").lower()
for letter in chosen_word:
  if letter == guess:
    print("right")
  else:
    print("wrong")

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
