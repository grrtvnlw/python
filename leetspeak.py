inp = input('Give me a string: ')

inp = inp.upper()

new_string = ''

for n in inp:
  if n == 'A':
    new_string += '4'
  elif n == 'E':
    new_string += '3'
  elif n == 'G':
    new_string += '6'
  elif n == 'I':
    new_string += '1'
  elif n == 'O':
    new_string += '0'
  elif n == 'S':
    new_string += '5'
  elif n == 'T':
    new_string += '7'
  else:
    new_string += n

print(new_string)