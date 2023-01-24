#     #####
#     #   #
#     #   #
#     #   #
#     #####
# Write a program to print the above pattern
n=int(input('Enter N:'))
for i in range (n):    
    for j in range (n):
        if(j==n-1 or j==0 or i==0 or i==n-1):
            print('#',end='')
        else:
            print(' ',end='')
    print('\n')
    
    
