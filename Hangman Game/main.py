import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

stage_level = len(stages)-1

# list of words the program will choose one of it
word_list = ["ardvark", "baboon", "camel", "flower", "bird", "crocodile"]

# randomly choosing a word
random_word = random.choice(word_list)
print(random_word)

# displaying the blanks of the chosen word
result = []
for _ in range(len(random_word)):
    result += "_"

print(result)


while(True):
    if "_" in result:
        # getting the user guess
        user_guess = input("Guess a letter: ").lower()
        if user_guess not in random_word:
            print(stages[stage_level])
            stage_level -= 1
            if stage_level == -1:
                print("You Lose")
                break
        else:
            for position in range(len(random_word)):
                if user_guess == random_word[position]:
                    result[position] = user_guess
        print(result)
    else:
        print("congratulations You saved the man!")
