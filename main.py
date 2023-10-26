import random

def play():
    words = ['phone camera', 'computer mouse', 'LED Lights', 'memory foam', 
             'CAT Scan', 'Joggers', 'Foil Blanket', 'Purifier', 'Dust Buster', 
             'Insulation', 'Jaws of Life', 'Laptop']
    used = []
    
    name = input("What is your name? ")

    while True:
        if len(used) == len(words):
            print("You've used all the words!")
            break

        word = random.choice(words)
        if word in used:
            continue

        used.append(word)
        print("Good Luck, " + name + "! Hint - some guesses are two words. A space could be a guess")

        guesses = ''
        turns = 12

        while turns > 0:
            failed = 0

            for char in word:
                if char in guesses:
                    print(char, end=" ")
                else:
                    print("_", end="")
                    failed += 1

            if failed == 0:
                print("\nYou win")
                print("The word is:", word)
                break

            print()
            guess = input("Guess a letter: ")
            guesses += guess

            if guess not in word:
                turns -= 1
                print("Wrong")
                print("You have", turns, "more guesses")

                if turns == 0:
                    print("You Lose")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

if __name__ == "__main__":
    play()
