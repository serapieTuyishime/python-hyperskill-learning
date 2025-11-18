# Description
# A good game needs a good interface. In this stage, you will make your output user-friendly.

# The player should be able to see the domino snake, the so-called playing field, and their own pieces. It's a good idea to enumerate these pieces because throughout the game the player will be selecting them to make a move.

# Two things must remain hidden from the player: the stock pieces and the computer's pieces. The player should not be able to see them, only the number of pieces remaining.

# Objectives
# Print the header using seventy equal sign characters (=).

# Print the number of dominoes remaining in the stock – Stock size: [number].

# Print the number of dominoes the computer has – Computer pieces: [number].

# Print the domino snake. At this stage, it consists of the only starting piece.

# Print the player's pieces, Your pieces:, and then one piece per line, enumerated.

# Print the status of the game:
# If status = "computer", print "Status: Computer is about to make a move. Press Enter to continue..."

# If status = "player", print "Status: It's your turn to make a move. Enter your command."
# Note that both these statuses suppose that the next move will be made, but at this stage, the program should stop here. We will implement other statuses (like "win", "lose", and "draw") in the stages to come.

# Examples
# Example 1

# The player makes the first move (status = "player")

# ======================================================================
# Stock size: 14
# Computer pieces: 6

# [6, 6]

# Your pieces:
# 1:[0, 6]
# 2:[5, 5]
# 3:[4, 4]
# 4:[4, 6]
# 5:[0, 1]
# 6:[0, 5]
# 7:[1, 6]

# Status: It's your turn to make a move. Enter your command.

# Example 2

# The Computer makes the first move (status = "computer")

# ======================================================================
# Stock size: 14
# Computer pieces: 7

# [5, 5]

# Your pieces:
# 1:[1, 3]
# 2:[1, 4]
# 3:[4, 5]
# 4:[1, 6]
# 5:[1, 1]
# 6:[0, 4]

# Status: Computer is about to make a move. Press Enter to continue...

import itertools
import random

next_player = {
    "pair": [-1, -1],
    "player": None
}
stock = []
player = []
computer = []
dominoes = []


def allocate_pieces(pieces):
    random.shuffle(pieces)
    player_pieces = pieces[0:7]
    computer_pieces = pieces[7:14]
    stock_pieces = pieces[14:]
    return player_pieces, computer_pieces, stock_pieces


def is_double(pair):
    return pair[0] == pair[1]


def is_next_player(double, player_):
    if next_player["pair"][0] < double[0]:
        next_player["pair"] = [double[0], double[1]]
        next_player["player"] = player_
    return


pairs = list(itertools.combinations_with_replacement(range(7), 2))
pairs = list(map(lambda x: list(x), pairs))

while next_player['pair'] == [-1, -1]:
    player, computer, stock = allocate_pieces(pairs)
    for (player_pair, computer_pair) in zip(player, computer):
        if is_double(player_pair):
            is_next_player(player_pair, "player")
        if is_double(computer_pair):
            is_next_player(computer_pair, "computer")

dominoes.append(next_player["pair"])
if next_player["player"] == "computer":
    double_s_index = computer.index(next_player["pair"])
    del computer[double_s_index]
else:
    double_s_index = player.index(next_player["pair"])
    del player[double_s_index]

print("=" * 70)
print(f"Stock size: {len(stock)}")
print(f"Computer pieces: {len(computer)}")
print()
print(next_player["pair"])
print()
print(f"Your pieces:")
for i,piece in enumerate(player):
    print(f"{i+1}:{piece}")
print()
if next_player["player"] == "computer":
    print("Status: It's your turn to make a move. Enter your command.")
else:
    print("Status: Computer is about to make a move. Press Enter to continue...")


