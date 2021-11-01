import random

# Gets 1000 most common English words
f = open('words.txt', 'r')
words = f.read().splitlines()
f.close()

# Declare constants
lives = 5
won = False
word_to_guess = random.choice(words)
chars = ["_ "] * len(word_to_guess)
guess = "".join(chars)

# Start game by printing number of letters
print(guess)

# Game loop
while lives > 0:
    letter = 'cum'
    # Player input
    # Repeat input of player until correct input
    while len(letter) > 1:
        print("Guess has to be only one letter!")
        letter = input("Guess a letter: ")
    
    # Change letter in display if letter in word_to_guess
    if letter in word_to_guess:
        for x, y in enumerate(word_to_guess):
            if y == letter:
                chars[x] = letter

    # Letter not in word: take one life
    else:
        print("That letter is not in the word. You now have {} lives".format(lives-1))
        lives -= 1

    # Print current progress
    guess = "".join(chars)
    print(guess)

    # Check if player has won
    if guess == word_to_guess:
        won = True
        print("You win!")
        break

# Check if player lost
if not won:
    print("You lose!")
    print("The word was {}".format(word_to_guess))
