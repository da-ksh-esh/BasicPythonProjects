import random 

def coin_toss():
    print("Coin Toss Game")
    choice = input("Heads or Tails? ").lower()
    result = random.choice(["heads", "tails"])
    if choice == result:
        print(f"It's {result} ! You win!")
    else:
        print(f"It's {result} ! You lose!")

coin_toss()