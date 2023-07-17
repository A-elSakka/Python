# Importing necessary libraries
import string
import secrets

# Defining the alphabet so we could randomise them later and making the alphabet
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = letters + digits + special_chars

# Making a fixed password length
pwd_length = 5

# Making the password based on the password length
pwd = ''
for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alphabet))

print(pwd)


