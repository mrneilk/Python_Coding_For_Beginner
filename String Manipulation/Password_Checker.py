# Input a password
# if its length is more than 6 and starts with a digit it is valid else it is invalid
password = input('Enter Password')
if len(password) > 6:
    if password[0].isdigit():
        print('Password accepted')
else:
    print('Invalid Password')