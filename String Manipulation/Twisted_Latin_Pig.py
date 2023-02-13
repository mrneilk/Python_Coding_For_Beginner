# Twisted Latin Pig
# Enter a word 
# Placa the first alphabet in last and add 'ay'
string = input('Enter String')
word = string[1:] + string[0] + 'ay'
print(word)