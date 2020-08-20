# print a triangle 
# set a variable for counter and user input
counter = 1
inp = int(input("How tall should we make this thing? "))

while counter <= inp:
    if counter == 1:
        print(" " * (inp - counter) + "*")
    else:
        print((" " * (inp - counter)) + ("*" * counter) + ("*" * (counter - 1)))
    counter += 1