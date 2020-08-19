width = int(input('Width? '))
height = int(input('Height? '))

print('*' * width)
for x in range(0, height - 2):
  print(('*' + (' ' * (width - 2)) + '*'))
print('*' * width)