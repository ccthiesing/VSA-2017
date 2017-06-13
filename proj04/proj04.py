# Name: Cameron Thiesing
# Date: 6-13-17

"""
proj04

Asks the user for a string and prints out whether or not the string is a palindrome.

"""

userstring = raw_input("Please enter a word or phrase:")
userstring = userstring.lower()
stringlist = []
nospace = []
for letter in userstring:
    stringlist.append(letter)
for letter in stringlist:
    if letter != ' ':
        nospace.append(letter)
while nospace:
    if nospace[0] == nospace[-1]:
        nospace = nospace[1:-1]
    else:
        print "This is not a palindrome."
        break
if len(nospace) == 0:
    print "This is a palindrome."
