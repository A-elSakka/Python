# Idea: Create a calculator that takes 3 inputs oprtr num1 num2 and calls the functions for each one of them to automatically do the math and print the answer

# Importing math
import math

# Taking the inputs from the user
oprtr_inpt = input("Which type of operator [+,-,*,/,**] ")
num1 = input("Enter your first number ")
num2 = input("Enter your second number ")

# Defining the 5 types of functions for each operator
def addtn(num1,num2):
    adtn_answer = int(num1)+int(num2)
    return adtn_answer
def sbtrct(num1,num2):
    sbtrct_answer = int(num1)-int(num2)
    return sbtrct_answer
def mltply(num1,num2):
    mltply_answer = int(num1)*int(num2)
    return mltply_answer
def dvsn(num1,num2):
    dvsn_answer = int(num1)/int(num2)
    return dvsn_answer
def pwr(num1,num2):
    pwr_answer = int(num1)**int(num2)
    return pwr_answer

if oprtr_inpt == "+":
    print(addtn(num1,num2))
elif oprtr_inpt == "-":
    print(sbtrct(num1,num2))
elif oprtr_inpt == "*":
    print(mltply(num1,num2))
elif oprtr_inpt == "/":
    print(dvsn(num1,num2))
elif oprtr_inpt == "**":
    print(pwr(num1,num2))
else:
    print("Wrong operator input")
