print('Welcome to the tip calculator')
bill = float(input('What was the total bill? $'))
people = int(input(('How many people to split the bill? ')))
percent = int(input(('What percentage tip would you like to give? 10, 12 or 15? %')))
print(f'Each person should pay: ${round(bill * (1 + percent / 100) / people, 1)}')

