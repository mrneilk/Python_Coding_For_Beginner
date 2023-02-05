# Series and Sequence 
# Print Series Starting from 1, 1, 2
# Every Next Number is defined as (prev1*prev2 + prev3)
# ....prev3, prev2, prev1, Nth Term
# Basically
# 1, 2, 2, 3, 7, 23, 164 ...

N = int(input("Enter the Number of Terms: "))

# setting up first three terms
n1, n2, n3 = 1, 1, 2
count = 0

# check if the number of terms is valid
if N < 3:
   print("Please enter a valid Term")
# if there is only one term, return n1
elif N == 3:
   print("sequence upto",N,":")
   print(n1," ",n2," ",n3)
# generate the  sequence
else:
   print("The sequence:",n1," ",n2," ",n3," ",end='')
   while count < N-3:
       nth=(n2*n3 + n1) 
       print(nth," ",end='')
       #nth = n1 + n2
       # update the previous term values
       n1 = n2
       n2 = n3
       n3 = nth
       count += 1
