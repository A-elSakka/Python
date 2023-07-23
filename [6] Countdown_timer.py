# Make a countdown app that gets inputted the required countdown in minutes and it just translates and goes

# Import time module 
import time

# Getting the input in minutes
inpt = int(input("Please enter your countdown timer [In Minutes] "))

# Conversion of minutes into seconds from the inpt
time_scnds = inpt * 60

# Countdown Loop
while time_scnds:
    minutes, seconds = divmod(time_scnds, 60)
    print(f"{minutes:02d}:{seconds:02d}",end="\r")
    time.sleep(1)
    time_scnds -= 1 
print(f"Times Up. Conclusion == {inpt} minutes have been counted")    
