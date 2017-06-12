# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""

#while loop

#userInput = int(raw_input("Enter a number: "))
#prevnum = 0
#Fibnum = 1
#while userInput > 0:
#    print Fibnum
 #   newnum = prevnum + Fibnum
#    prevnum = Fibnum
 #   Fibnum = newnum
#    userInput -= 1

#For loop

userInput = int(raw_input("Enter a number: "))
prevnum = 0
fibnum = 1
for number in range(userInput):
    print fibnum
    newnum = fibnum + prevnum
    prevnum = fibnum
    fibnum = newnum



