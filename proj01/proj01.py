# Name: Cameron Thiesing
# Date: 6-12-17

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!
# I divided the string the user gave me (being their name) into the first letter and the rest of the name. I then commanded the computer to
# capitalize the first letter. Then at the end I added the parts of the name back together.


user_input = raw_input("Enter your name:")
capital = user_input[0]
Rest = user_input[1:]
user_input2 = capital.upper()
user_inputAge = raw_input("Enter your age:")
user_inputBirthday = raw_input("Have you had a birthday this year? ")
if user_inputBirthday == "yes":
    user_inputAgeint = int(user_inputAge)
    TimeLeft = 100 - user_inputAgeint
    year = TimeLeft + 2017
else:
    user_inputAgeint = int(user_inputAge)
    TimeLeft = 99 - user_inputAgeint
    year = TimeLeft + 2017
print str(user_input2) + str(Rest) + " will turn 100 in the year " + str(year) + "!"
if user_inputAge < 16:
    print "PS: you can see R, PG-13, PG, or G movies"
elif user_inputAge >= 13:
    print "PS: you can see PG-13, PG, or G movies"
else:
    print "PS: you can see PG or G movies"
