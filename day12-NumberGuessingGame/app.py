from random import randint

print("Welcome To Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

difficulty = input("Please choose a difficulty level: easy, or hard: ")

if difficulty == "easy":
    number_of_attempts = 10
elif difficulty == "hard":
    number_of_attempts = 5

number = randint(1, 100)

print(f"You have {number_of_attempts} attempts to guess the number.")

while number_of_attempts > 0:
    guess = int(input("Guess a number: "))
    if guess == number:
        print(":)")
        print("You guessed the number!")
        break
    elif guess > number:
        print("__Too high.__")
    elif guess < number:
        print("__Too low.__")
    number_of_attempts -= 1
    if number_of_attempts == 0:
        print(":(")
        print("You ran out of attempts.")
        print(f"The number was {number}.")
        print("Game Over!")
        break
    else:
        print(f"You have {number_of_attempts} attempts to guess the number.")
        print("Guess again!")
        continue
