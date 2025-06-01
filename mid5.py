rendomNumber = int(input("Put a number: "))
sum = 0;
while rendomNumber>0:
  remainder=rendomNumber%10
  rendomNumber//=10
  sum+=remainder
print ('the guessing num: ', sum)