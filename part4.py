import random

with open("assets/words_alpha.txt", "r") as f:
    random_word_list = f.read().splitlines()

print("Word Guessing Game")

wins = 0
losses = 0
game_over = False
round_over = False
while not game_over:
    random_word = random.choice(random_word_list)
    random_word_list.remove(random_word)

    hidden_word = ""
    for l in random_word:
        hidden_word += "_"

    player_guesses = 0
    guessed_letters = []
    win = False

    while not round_over:
        print("Your word is " + hidden_word + " and you have " + str(7 - player_guesses) + " guesses left.")
        player_guess = input("press 1 to guess letter, 2 to guess word, 3 to exit: ")

        if player_guess == "1":
            letter = input("")

            if letter in guessed_letters or len(letter) != 1:
                print("invalid guess, try again")
                continue

            else:
                guessed_letters.append(letter)
                player_guesses += 1
                i = 0

                for l in random_word:
                    if letter == l:
                        hidden_word_list = [char for char in hidden_word]
                        hidden_word_list[i] = letter
                        hidden_word = "".join(hidden_word_list)
                    i += 1

                if hidden_word == random_word:
                    win = True

        elif player_guess == "2":
            word = input("")

            if(len(word) != len(random_word)):
                print("invalid guess, try again")
                continue

            else:
                player_guesses += 1

                if(word == random_word):
                    win = True

                else:
                    print("wrong guess")

        elif player_guess == "3":
            losses += 1
            round_over = True

        else:
            print("invalid option, try again")

        if win:
            print("Nice win! It took you " + str(player_guesses) + " guesses.")
            wins += 1
            round_over = True

        elif player_guesses == 7:
            print("You lost. The word was " + random_word + ". Better luck next time!")
            losses += 1
            round_over = True

    print("Your score is " + str(wins) + " wins and " + str(losses) + " losses.")

    play_again = input("press 1 to play again, 2 to exit: ")

    if play_again == "1":
        round_over = False
    
    elif play_again == "2":
        game_over = True
