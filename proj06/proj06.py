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

guessesL = 6
def correct():
    yes = False
    for letter in word2:
        if letter in answer1:
            print "ALAS! YOU HAVE GUESSED A LETTER!"
            yes = True
            for num in range(len(word2)):
                if word2[num] == letter:
                    blanks[num] = letter
                    word2[0] = word2[1]

            break
    return yes
alpha = []
word2 = []
word = choose_word(wordlist)
for stuff in string.lowercase:
    alpha.append(stuff)
for letter in word:
    word2.append(letter)
blanks = []
for item in word2:
    blanks.append('_')

print "WELCOME TO THE HANGMAN: THE GAME!"
print "THE WORD I HAVE SELECTED IS", len(word2), "LETTERS LONG."
while guessesL > 0:
    print blanks
    print word
    print  "YOU CAN USE THESE LETTERS: ", alpha
    print "YOU HAVE ", str(guessesL), "GUESSES LEFT."
    answer1 = raw_input("GUESS!!")
    correct()
    if correct() == False:
        guessesL = guessesL - 1
        print "SORRY, THAT WAS INCORRECT."
    for letter in alpha:
        if letter in answer1:
            for num in range(len(alpha)):
                if alpha[num] == letter:
                    alpha[num] = "_"
    if len(word2) == 0:
        print "I HAVE BEEN DEFEATED! YOU GUESSED THE WORD:"
        print word
        break
if guessesL == 0:
    print "YOU HAVE BEEN DEFEATED!! YOU WERE UNABLE TO GUESS THE WORD:"
    print word