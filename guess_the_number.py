import random

print('I am thinking of a number between 1 and 10.')

num = random.randint(1, 10)
guesses = 5

while True:
  if guesses > 0:
    print(f'You have {guesses} guesses left.')
    guess = int(input('What\'s the number? '))
    
    if guess == num:
      print('Yes! You win!')
      break
    elif guess > num:
      print(f'{guess} is too high.')
      guesses -= 1
    elif guess < num:
      print(f'{guess} is too low.')
      guesses -= 1
  else:
    print('You ran out of guesses!')
    break