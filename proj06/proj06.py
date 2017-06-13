# Name: Cameron
# Date: 6-13-17


# proj06: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()
# your code begins here!
#functions:
def guesses():
    guessesL = [6]
    print "YOU HAVE ", len(guessesL), "LEFT."


def correct():
    yes = False
    for letter in word2:
        if letter in answer1:
            print "ALAS! YOU HAVE GUESSED A LETTER!"
            yes = True
    return yes


word = choose_word(wordlist)
word2 = []
for letter in word:
    word2.append(letter)
print "WELCOME TO THE HANGMAN: THE GAME!"
print "THE WORD I HAVE SELECTED IS", len(word2), "LETTERS LONG."
print word
answer1 = raw_input("DO YOU DARE GUESS MY WORD?")
correct()


