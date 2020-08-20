my_nums = [10, 20, 30, 99, 50, 12, 87, 90, 1, 101, 9182691, 12, -11, 42]

new_nums = []

for number in my_nums:
  if number >= 0 and number % 2 == 0:
    new_nums.append(number)

print(new_nums)