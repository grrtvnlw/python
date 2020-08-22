def charCount(inp):
  result = {}

  inp = inp.lower()

  for letter in inp:
    if letter.isalpha():
      if letter in result.keys():
        result[letter] += 1
      else:
        result[letter] = 1

  return result

print(charCount('Hi there'))