# inp = input('Give me a word: ')

# vowels = 'aeiouyAEIOUY'
# prev_letter = ''

# new_string = ''

# for letter in inp:
#   if letter in vowels:
#     if letter == prev_letter:
#       new_string += letter * 4
#     else:
#       new_string += letter
#   else:
#     new_string += letter

#   prev_letter = letter

# print(new_string)

inp = input('Give me a word: ')

vowels = 'aeiouyAEIOUY'

new_string = ''

for index in range(len(inp)):
  if inp[index] in vowels and (index + 1) < len(inp):
    if inp[index] == inp[index + 1]:
      new_string += inp[index] * 4
    else:
      new_string += inp[index]
  else:
    new_string += inp[index]

print(new_string)