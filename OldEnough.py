# OldEnough.py
# Billy Ridgeway
# Finds out if you're old enough to drive in where you live
#  and calculate how many years you have to wait if you are not.

# Asks the user for the legal driving age where they live.
driving_age = eval(input("What is the legal driving age where you live? "))

# Asks the user how old they are.
your_age = eval(input("How old are you? "))

# If the user's age is greater than or equal to the legal age the program
# will display that they are old enough to drive.
if your_age >= driving_age:
    print("You're old enough to drive!")

# If the user's age is less than the legal age, the program will display
# a message that they can't drive and calculate how many years it will
# be until they are of legal age to drive.
else:
    print("Sorry, you can drive in", driving_age - your_age, "years.")
    


#if your_age < driving_age:
    #print("Sorry, you can drive in", driving_age - your_age, "years.")
