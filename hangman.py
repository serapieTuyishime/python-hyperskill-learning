## Write your code here
from random import choice
import re

wordList = ["python", "java", "swift", "javascript"]
trials = 8
word = choice(wordList)
final_result = '-' * len(list(word))
attempts = []
wins = 0
losses = 0


def record_score(decision):
    global attempts, word, final_result, wins, losses
    attempts = []
    word = choice(wordList)
    final_result = '-' * len(list(word))
    if decision == 'win':
        wins += 1
    elif decision == 'loss':
        losses += 1


def reduce_lives():
    global trials
    trials -= 1


def hangman(character):
    global final_result
    if character in final_result:
        print("No improvements.")
        reduce_lives()

    elif character in word:
        previous_index = -1
        while True:
            index = word.index(character, previous_index + 1)
            final_result = final_result[:index] + character + final_result[index + 1:]

            previous_index = index
            if (final_result.count(character) == word.count(character) or
                    word.count(character) == 1):
                break
    else:
        reduce_lives()
        print("That letter doesn't appear in the word. ")


print("H A N G M A N")
while True:
    user_request = input("Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit: ")
    if user_request == "exit":
        break
    elif user_request == "results":
        print(f"You won {wins} times.\nYou lost: {losses} times.")

    elif user_request == "play":
        while True:
            if final_result == word:
                print(f"You guessed the word {word}!")
                record_score("win")
                print("You survived!")
                break
            elif trials == 0:
                print("Thanks for playing!")
                record_score("loss")
                print("You lost!")
                break

            user_input = input(f"""
{final_result}
Input a letter:""")

            if len(user_input) > 1 or len(user_input) == 0:
                print("Please, input a single letter")

            elif not re.match(r'^[a-z]+$', user_input):
                print("Please, enter a lowercase letter from the English alphabet")

            elif user_input in attempts:
                print("You've already guessed this letter.")
            else:
                attempts.append(user_input)
                hangman(user_input)
