# greeting
print('Welcome to the tip calculator! ')

# store bill total
bill = float(input('What was the total bill? '))

# store reqesed tip
tip = int(input('How much of a tip would you like to give? '
            + '10, 15, or 15? '))

# calculate tip
tip = bill*(tip * .01)

# store num of people to split bill
people = int(input('How many people to split the bill? '))

#calculte cost per person
costPerPerson = round(((bill + tip)/people), 2)

# output cost
print(f'Each person should pay {costPerPerson} ')