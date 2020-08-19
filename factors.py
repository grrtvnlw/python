num = int(input('Give me a number: '))
count = 1

while count <= num:
  if num % count == 0:
    print(count)
  count += 1