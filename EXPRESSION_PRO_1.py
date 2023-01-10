# Program to convert height form centimetres to feet and inches
h1 = float(input('Enter height in cm:'))
feet = int(h1/30.48)
inches = int((h1/2.54)%12)
print('Your Height is ',feet,' feet ', inches, ' inches')
