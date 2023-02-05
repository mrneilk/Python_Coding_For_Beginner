# Program to First ten prime Numbers using loops
# Reference: https://www.geeksforgeeks.org/generate-and-print-first-n-prime-numbers/
import math                                                 # Import Math Library for square root, and Floor function 
X = 0
i = 2
flag = False                                                # Declare a Boolean variable flag False
while(X < 10):
  flag = True
  for j in range(2, math.floor(math.sqrt(i)) + 1):          # Main Conditional loop, checks for prime number
    if (i%j == 0):
      flag = False
      break
  if(flag):
      print(i, end=" ")
      X+=1
  i+=1
print()
