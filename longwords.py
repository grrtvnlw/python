inp = input('Give me a word: ')

vowels = 'aeiouy'

new_string = ''

for (first, second) in inp:
  if first == second:
    if first in vowels:
      new_string += first * 4
    else:
      new_string += first
  else: 
    new_string += first

print(new_string)