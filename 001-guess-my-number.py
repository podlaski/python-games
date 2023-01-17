# Game "Guess my number"

import random

name = input("What is your name? ")
number = random.randint(1,10)

print(f"\nHello {name}, I'm thinking of a number between 1 and 10.\nPlease guess what number it is.\nYou can try 5 times.")

def counting_down():
    repeat = 5
    repeat = repeat - 1
    print(f"You have only {repeat} tries.")

for guess in range(5):
    guess = input("Your number: ")
    guess = int(guess)

    if guess < number:
        print("\nYour number is too low.")
        counting_down()
    if guess > number:
        print("\nYour number is too high.")
        counting_down()
    if guess == number:
        break

if guess != number:
    print("\nIt failed. You've used all the trials.\n")    

if guess == number:
    print(f"\nVery Good {name}! That is my number!\n")
