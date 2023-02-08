# Write a loop that print out index of every 'i' in 'Mississippi'
word = "Mississippi"
ind = 0
for char in word:
    if char == 'i':
        ind = word.index(char,ind+1)
        print(ind)
        
