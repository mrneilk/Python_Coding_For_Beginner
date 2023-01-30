# ######
#  # 
#   #
#    #
#     #
#      #
# ######
# Print The following Pattern
n=int(input('Enter N:'))    # input the size
for i in range (n):     
    for j in range (n):
        if(j==n-i or i==0 or i==n-1):       # Print in first and last rows and Print in each row with col=size-row number
            print('#',end='')
        else:
            print(' ',end='')
    print('\n')
