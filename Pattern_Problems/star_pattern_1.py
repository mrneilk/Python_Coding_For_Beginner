# Print the following patter with user inputting the height of pattern
# *****
# ****
# ***
# **
# *
n =int(input('Enter the Height of Pattern'))
for i in range (n,0,-1):    # Running the loop in reverse
    for j in range (0,i):
        print('*',end='')
    print('\n')
    n=n-1
    
