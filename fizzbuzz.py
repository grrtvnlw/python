inp = int(input('Give me a number: '))

counter = inp

while counter > 0:
  isFizz = counter % 3 == 0
  isBuzz = counter % 5 == 0

  if isFizz and isBuzz:
    print('fizzbuzz')
  elif isFizz:
    print('fizz')
  elif isBuzz:
    print('buzz')
  else:
    print(int(counter))
  
  counter -= 1