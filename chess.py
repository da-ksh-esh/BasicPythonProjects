col = input('Enter column letter: ')
row = int(input('Enter row number: '))

if row % 2 != 0 and col in ['a', 'c', 'e', 'g']:
    print(f'{col}{row} is Black')
elif row % 2 == 0 and col in ['a', 'c', 'e', 'g']:
    print(f'{col}{row} is White')
elif row % 2 == 0 and col in ['b', 'd', 'f', 'h']:
    print(f'{col}{row} is black')
elif row % 2 != 0 and col in ['b', 'd', 'f', 'h']:
    print(f'{col}{row} is White')
else:
    print('Enter a valid position')