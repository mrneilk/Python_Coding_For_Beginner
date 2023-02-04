# Fiboncii Series
# Fn = Fn-1 + Fn-2

N = int(input("Enter the Number of Terms: "))

# setting up first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if N <= 0:
   print("Please enter a valid Term")
# if there is only one term, return n1
elif N == 1:
   print("Fibonacci sequence upto",N,":")
   print(n1)
# generate the fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < N:
       print(n1,end='')
       nth = n1 + n2
       # update the previous term values
       n1 = n2
       n2 = nth
       count += 1
