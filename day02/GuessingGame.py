import random
import time

# GUESSING GAME

# Create a number guessing game!

# A number between one and a hundred will be choosen randomly by the method 'random', then the user will try to guess it. 
# Each time the user guesses it, it will be displayed whether they should guess higher, or lower next time. So that, eventually they will get the right number.
# It will also be shown how many times it took for the user the guess the correct number.

print("Welcome to the Guessing Game! I'm going to select a secret number between 01 and 100.")
time.sleep(4)

print("Picking a number...")
time.sleep(3)

print("Let's play!! Please, pick a number from 01 to 100. What is your guess? ")

guess = int(input(''))
correct_number = random.randint(1, 100)
guess_count = 1

while guess != correct_number:
  time.sleep(1)
  guess_count += 1
  if guess < correct_number:
    guess = int(input("Incorrect! You should guess higher. What is your guess? "))
  else:
    guess = int(input("Incorrect! You should guess lower. What is your guess? "))
      
print(f"Congrats!! The right answer is {correct_number}. It took you only {guess_count} guesses!") 

# ===========================================================

