# Idea : A program where it takes your input for a number and generating a random number of a range of anything and checking if the number is less than or bigger than the inputted number
 
# Importing necessary modules
import random # For randomization

# Taking the user's input of the number between [1-100]
guess = int(input("Please enter a number between [1-100] "))

# Creating the randomization function
def rndmiz_num(num):
    answr = random.randint(1,100)
    if answr == num:
        print("Congratulations. You have won. ")
    elif answr < num:
        print("A little higher you should go. ")
    else:
        print("A little lower you should go. ")

# Creating a function to check if the input is int or not
def check_guess(guess):
    if guess == int(guess):
        print(rndmiz_num(guess))

check_guess(guess)

