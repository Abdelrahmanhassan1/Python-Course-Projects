import random
from hangman_art import logo, stages
from hangman_words import word_list

stage_level = len(stages)-1

# randomly choosing a word
random_word = random.choice(word_list)
# print(random_word)

# displaying the blanks of the chosen word
result = []
for _ in range(len(random_word)):
    result += "_"

print(logo)

print(f"{' '.join(result)}")
print()

while(True):
    if "_" in result:
        # getting the user guess
        user_guess = input("Guess a letter: ").lower()
        if user_guess not in random_word:
            print(stages[stage_level])
            print(
                f"You guessed {user_guess}, that's not in the word. You lose a life.")
            print(f"You have {stage_level} lives.")
            stage_level -= 1
            if stage_level == -1:
                print("You Lose")
                break
        elif user_guess in result:
            print(f"You've already guessed {user_guess}")
        else:
            for position in range(len(random_word)):
                if user_guess == random_word[position]:
                    result[position] = user_guess
        print(f"{' '.join(result)}")
        print("===========================================================================")
    else:
        print("congratulations You saved the man!")

print("===========================================================================")
