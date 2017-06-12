# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
import random
compnumber = random.randint(1,9)
print compnumber
level = raw_input("DO YOU WANT HARD OR EASY?")
userinput = int(raw_input("What number am I thinking of? (you have 4 guesses)"))
guesses = 0
numguesses = 3
if level == "easy":
    while numguesses > 0:
        if userinput == compnumber:
            guesses += 1
            numguesses -= 1
            print "GOOD JOB! YOU TOOK " + str(guesses) + " GUESSES."
            break
        if userinput > compnumber:
            guesses += 1
            numguesses -= 1
            print "NOPE! TOO HIGH!"
            userinput = int(raw_input("GUESS AGAIN!"))
        if userinput < compnumber:
            guesses += 1
            numguesses -= 1
            print "NOPE! TOO LOW!"
            userinput = int(raw_input("GUESS AGAIN!"))
        if numguesses == 0:
            print "SORRY! BETTER LUCK NEXT TIME! THE NUMBER WAS " + str(compnumber)
else:
    while numguesses > 0:
        if userinput == compnumber:
            guesses += 1
            numguesses -= 1
            print "GOOD JOB! YOU TOOK " + str(guesses) + " GUESSES."
            break
        if userinput != compnumber:
            guesses += 1
            numguesses -= 1
            print "NOPE!"
            userinput = int(raw_input("GUESS AGAIN!"))
        if numguesses < 0:
            print "SORRY! BETTER LUCK NEXT TIME! THE NUMBER WAS " + str(compnumber)
            break
