# input a word and print "yes it starts!!" if the word starts with '0' '1' '2' ... '9'.
word = input('Enter the word')
try:
    num = int(word[0])
    if num >= 0 and num <= 9:
        print("Yes It Starts")
except:
    print("No")
