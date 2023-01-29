# ######
#     # 
#    #
#   #
#  #
# #
# ######
# Print The following Pattern
n=int(input('Enter N:'))
for i in range (n):    
    for j in range (n):
        if(j==n-i or i==0 or i==n-1):
            print('#',end='')
        else:
            print(' ',end='')
    print('\n')
    
    
