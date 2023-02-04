# 8
# 86
# 864
# 8642
# Write a script that print the above pattern
n=int(input('Enter H:'))
for i in range (n):    
    num=8
    for j in range (i):
        print(num,end='')
        num=num-2
    print('\n')
    
    
