coins = 0

while True:
  print(f'You have {coins} coins.')
  inp = input('Do you want another? ').lower()

  if inp == 'yes':
    coins += 1
  else:
    print('Bye')
    break
