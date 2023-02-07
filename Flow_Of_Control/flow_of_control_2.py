#Enter marks of three subject and find average and give them grade according to the percentage
m1=int(input('Marks Sub 1:'))
m2=int(input('Marks Sub 1:'))
m3=int(input('Marks Sub 1:'))
avg=(m1+m2+m3)/3
print('Average:',avg)
print('Grade:')
if avg>=80:
  print('A')
elif avg>=70 && avg<=79:
  print('B')
elif avg>=60 && avg<=69:
  print('C')
elif avg>=50 && avg<=59:
  print('D')
elif avg>=40 && avg<=49:
  print('E')
else:
  print('F')
