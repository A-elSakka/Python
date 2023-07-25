# Bank application that uses a class to make a deposit/withdraw/and show available balance
# Deposit[1], Withdraw[2], Balance[3]

# Deposit function containing the value of the balance of the account in which you can deposit/withdraw
balance = 100 # A global balance so it can be saved as long as the user is in the app

def begin():
    print("Hello There, Welcome to Sakka banking's, We are so happy to have you here. ")
    print("--------------------------------------------------------------------------")
    print("Please choose from the numbers to select an option to begin a transaction")
    print("[1] ---->> Deposit ")
    print("[2] ---->> Withdraw ")
    print("[3] ---->> Balance ")

def trans_chck():
    inpt = input("Please select a number from below. ")
    inpt = int(inpt)
    try:
        if inpt not in [1,2,3]:
            raise ValueError("Invalid input, Try again.")
        if inpt == 1:
            dpsit()
        elif inpt == 2:
            wthdrw()
        elif inpt == 3:
            bal()
    except ValueError:
        print("Unkown input. Please try again. ")
        begin()


def dpsit():
    global balance
    amount = input("Please enter the amount of money you want to deposit. ")
    try:
        amount = int(amount)
        balance += amount
        print(balance)
    except(ValueError):
        print("Error:404<<<-------->>> Please Try Again. ")
        begin()
    

def wthdrw():
    global balance
    amount = input("Please enter the amount of money you want to withdraw. ")
    try:
        amount = int(amount)
        balance -= amount
        print(balance)
    except(ValueError):
        print("Error:404<<<-------->>> Please Try Again. ")
        return
        begin()
    if amount > balance:
        print("Error:404<<<-------->>> Please Try Again. ")
        print("Not enough balance you got bud ")
        begin()

def bal():
    global balance
    print(balance)

begin()
trans_chck()