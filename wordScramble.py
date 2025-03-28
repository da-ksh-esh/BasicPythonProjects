import random
def scramble_word(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

def word_scramble():
    word = ["python", "javascript", "scramble", "coding", "computer"]
    word = random.choice(word)
    scrambled_word = scramble_word(word)

    print("Word Scramble Game")
    print(f"Unscramble the word: {scrambled_word}")
    guess = input("Your guess: ")

    if guess == word:
        print("Correct! Your unscrambled the word.")
    else:
        print(f"Wrong! The correct word was {word}.")

word_scramble()