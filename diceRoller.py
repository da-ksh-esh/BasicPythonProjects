import random

def roll_dice():
    print('Dice Roller')
    while True:
        input("Press Enter to roll the dice...")
        result = random.randint(1,6)
        print(f"Your rolled a {result}")
        play_again = input("Roll again? (y/n): ")
        if play_again.lower() != 'y':
            break

roll_dice()        