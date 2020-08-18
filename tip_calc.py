# write a tip calculator based off user input and quality of service
# get user input for total bill amount, quality of service, and tip amount
total_bill = float(input("Total bill amount? "))
service_level = input("Level of service - good, fair, or bad? ")

# calculate tip based off user input
if service_level == "good":
    tip = total_bill * .20
elif service_level == "fair":
    tip = total_bill * .15
elif service_level == "bad":
    tip = total_bill * .10

# format tip and bill to dollar amount and calculate total bill including tip
format_tip = '%.2f' % tip
total_bill += tip
format_total_bill = '%.2f' % total_bill

# display formatted output
print(f"Tip amount: ${format_tip}")
print(f"Total amount: ${format_total_bill}")

##############################################

bill = float(input('Total bill amount? '))
service = input('Level of service? ')

if service == 'good':
  tip = bill * .20
  bill = bill + tip
  tip = '${:,.2f}'.format(tip)
  bill = '${:,.2f}'.format(bill)
  print(f'Tip amount: {tip}')
  print(f'Bill amount: {bill}')
elif service == 'fair':
  tip = bill * .15
  bill = bill + tip
  tip = '${:,.2f}'.format(tip)
  bill = '${:,.2f}'.format(bill)
  print(f'Tip amount: {tip}')
  print(f'Bill amount: {bill}')
elif service == 'bad':
  tip = bill * .10
  bill = bill + tip
  tip = '${:,.2f}'.format(tip)
  bill = '${:,.2f}'.format(bill)
  print(f'Tip amount: {tip}')
  print(f'Bill amount: {bill}')
else:
  print('Invalid input - try again')