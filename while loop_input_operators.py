def guessing_game():
    secret_num = 7
    num_guesses = 0
    guess_num = False
    print("Total number of guesses made:", num_guesses)
    while not guess_num:
        guess = int(input("Guess a number between 1 and 10: "))
        num_guesses += 1
        if guess == secret_num:
            print("Correct! You guessed the secret number in", num_guesses, "guesses.")
            guess_num = True
        else:
            print("Not quite. Try again.")
            print("Total number of guesses made:", num_guesses)
guessing_game()