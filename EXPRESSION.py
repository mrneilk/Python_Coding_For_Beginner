#program to calculate simple interest and compound interest
p=float(input('enter principle amount:'))
r=float(input('enter rate of interest:'))
t=float(input('enter time period in year:'))
print('The Simple Interest: ',p*r*t/100)
print('The compound interest compounded annually: ',p*((1+(r/100))**t)-p)
