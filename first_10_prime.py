# Program to First ten prime Numbers using loops
# Reference: https://www.geeksforgeeks.org/generate-and-print-first-n-prime-numbers/
import math
X = 0
i = 2
flag = False
while(X < 10):
  flag = True
  for j in range(2, math.floor(math.sqrt(i)) + 1):
    if (i%j == 0):
      flag = False
      break
  if(flag):
      print(i, end=" ")
      X+=1
  i+=1
print()
