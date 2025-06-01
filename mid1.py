str = input('enter a number: ')
print(str)
i = 0
while i<len(str)/2:
  str[i], str[len(str)-i-1] = str[len(str)-i-1], str[i]
  i+=1
  print(str)