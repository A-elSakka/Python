# Program giving me specific outputs [Have to be runned manually] to remind me that am in life and everything is shit [Recommended Time: Mornings]
# data about me 
# Importing datetime module
import datetime
import calendar # for day name

# Function to translate the name of the day according to numbers
def calc_day(function):
    if function == 0 :
        return "Monday"
    elif function == 1 :
        return "Tuesday"
    elif function == 2 :
        return "Wednesday"
    elif function == 3 :
        return"Thursday"
    elif function == 4 :
        return "Friday"
    elif function == 5 :
        return "Saturday"
    elif function == 6:
        return "Sunday"
    else:
        print("Invalid Code")

# Age function
def main():
    # Getting todays day/date
    today = datetime.date.today()
    current_date = today
    bornday = datetime.date(2007,3,5)
    age = today.year - bornday.year - ((today.month, today.day) < (bornday.month, bornday.day))
    print("Your full name is",full_name)
    print(msg)
    print(str(age)," Years Old")
    print("Born on",str((bornday)))
    print(("We are on this year, Crazy Right!? "+str(today.year)))
    print("This is the day in numbers",str(today.day))
    print("Today is",calc_day(current_date.weekday()))
    print("Today's date == ", str(datetime.date.today()))


# Info Variables
full_name = "Ahmed Abdelsalam Alsakka"
name = "Ahmed"
family = "[3 including me] brother + sister + me"
schol_yr = "1st Secondary"
schol_nme = "American Language School in Qwesna"
goals = "I love computer/Programming/Coding I want to be a IT/Engineer/Fullstack developer"
msg = "Hey this is a msg for 16 yr old ahmed, Love Ya Bro , Keep on Going, You're in the Clear"
main()






