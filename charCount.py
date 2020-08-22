'hello' # {h: 1, e: 1, l: 2, o: 1}

'Hi hello' # {H: 1, ' ': 1, h: 1, e: 1, l: 2, o: 1}

def charCount(inp):
  result = {}

  for letter in inp:
    if letter in result.keys():
      result[letter] += 1
    else:
      result[letter] = 1

  return result

print(charCount('Hi there'))