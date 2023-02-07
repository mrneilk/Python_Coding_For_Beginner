# input a list from user
# give choice to print sum of positive even number, positive odd numbers and sum of negative numbers
# end the scipt if user enters 0(zero)
# creating an empty list
numList = []
  
# number of elements as input
n = int(input("Enter number of elements : "))
  
# iterating till the range
for i in range(0, n):
    ele = int(input())
  
    numList.append(ele) # adding the element

sumEven = 0
sumOdd = 0
sumNeg = 0
for i in range(0, n):
    if numList[i] > 0 and numList[i]%2 == 0:
        sumEven += numList[i]
    if numList[i] > 0 and numList[i]%2 != 0:
        sumOdd += numList[i]
    if numList[i] < 0:
        sumNeg += numList[i]

ch = int(input("Enter Choice 1) Sum off positive even\n 2) Sum off positive odd\n 3) Sum off negative\n"))

if ch == 1:
    print(sumEven)
elif ch == 2:
    print(sumOdd)
elif ch == 3:
    print(sumNeg)
elif ch == 0:
    print("You Entered 0 ending")