# Simple FizzBuzz Program , if number is divisible by 3 and 5 print FizzBuzz if number divisible by only 3 print Fizz and 
# if number only divisible by 5 print Buzz if not any one of them print the number
# range of number is from 1 to 100
for i in range(1,100):
  if (i%3==0 and i%5==0):
    print("FizzBuzz")
  elif(i%3==0):
     print("Fizz")
  elif(i%5==0):
     print("Buzz")
   else:
     print(i)
