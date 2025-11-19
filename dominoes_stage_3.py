Description
It's time to bring the game to life. In this stage, you need to add a game loop that will allow players to take turns until the end-game condition is met.

In dominoes, you can make a move by taking one of the following actions:

Select a domino and place it on the right side of the snake.

Select a domino and place it on the left side of the snake.

Take an extra piece from the stock (if it's not empty) and skip a turn.

To make a move, the player has to specify the action they want to take. In this project, the actions are represented by integer numbers in the following manner: {side_of_the_snake (+/-), domino_number (integer)} or {0}. For example:
-6 : Take the sixth domino and place it on the left side of the snake.
6 : Take the sixth domino and place it on the right side of the snake.
0 : Take an extra piece from the stock (if it's not empty) and skip a turn or simply skip a turn if the stock is already empty by this point.

When it's time for the player to make a move, your program must prompt the user for a number. If this number exceeds the limitations (larger than the number of dominoes), your program must generate an error message and prompt for input again. Once the valid input is received, your program must apply the move.

For now, don't bother about the AI, our goal is just to make the game playable. So, when it's time for the computer to make a move, make it choose a random number between -computer_size and computer_size (where the computer_size is the number of dominoes the computer has).

The end-game condition can be achieved in two ways:

One of the players runs out of pieces. The first player to do so is considered a winner.

The numbers on the ends of the snake are identical and appear within the snake 8 times. For example, the snake below will satisfy this condition:
[5,5],[5,2],[2,1],[1,5],[5,4],[4,0],[0,5],[5,3],[3,6],[6,5]
These two snakes, however, will not:
[5,5],[5,2],[2,1],[1,5],[5,4],[4,0],[0,5]
[6,5],[5,5],[5,2],[2,1],[1,5],[5,4],[4,0],[0,5],[5,3],[3,1]
If this condition is satisfied, it is no longer possible to go on with this snake. Even after emptying the stock, no player will have the necessary piece. Essentially, the game has come to a permanent stop, so we have a draw.

When the game ends, your program should print the result.

Throughout the gameplay, the snake will grow in length. If it gets too large, the interface might get ugly. To avoid this problem, draw only the first and the last three pieces of the snake, separate them by three dots, ..., for example, [3, 5][2, 2][6, 6]...[3, 6][0, 3][3, 4].

Objectives
Modify your Stage 2 code:

At the end of the game, print one of the following phrases:
Status: The game is over. You won!
Status: The game is over. The computer won!
Status: The game is over. It's a draw!

Print only the first and the last three pieces of the domino snake separated by three dots if it exceeds six dominoes in length.

Add a game loop that will repeat the following steps until the game ends:

Display the current playing field (stage 2).

If it's a user's turn, prompt the user for a move and apply it. If the input is invalid (its value is not-integer or it exceeds limitations), request a new input with the following message: Invalid input. Please try again..

If it's a computer's turn, prompt the user to press Enter, randomly generate a move, and apply it.

Switch turns.

Keep in mind that at this stage we have no rules! Both the player and the computer can place their dominoes however they like.

Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1

Typical gameplay.

======================================================================
Stock size: 14
Computer pieces: 6

[6, 6]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[4, 6]
5:[0, 1]
6:[0, 5]
7:[1, 6]

Status: It's your turn to make a move. Enter your command.
> 4
======================================================================
Stock size: 14
Computer pieces: 6

[6, 6][4, 6]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[0, 1]
5:[0, 5]
6:[1, 6]

Status: Computer is about to make a move. Press Enter to continue...
>
======================================================================
Stock size: 14
Computer pieces: 5

[6, 6][4, 6][1, 3]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[0, 1]
5:[0, 5]
6:[1, 6]

Status: It's your turn to make a move. Enter your command.
> -6
======================================================================
Stock size: 14
Computer pieces: 5

[1, 6][6, 6][4, 6][1, 3]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[0, 1]
5:[0, 5]

Status: Computer is about to make a move. Press Enter to continue...
>
======================================================================
Stock size: 13
Computer pieces: 6

[1, 6][6, 6][4, 6][1, 3]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[0, 1]
5:[0, 5]

Status: It's your turn to make a move. Enter your command.
> 0
======================================================================
Stock size: 12
Computer pieces: 6

[1, 6][6, 6][4, 6][1, 3]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[0, 1]
5:[0, 5]
6:[2, 3]

Status: Computer is about to make a move. Press Enter to continue...
>


Example 2

Invalid input.

======================================================================
Stock size: 14
Computer pieces: 5

[4, 4][2, 3][3, 4]

Your pieces:
1:[1, 2]
2:[2, 6]
3:[0, 4]
4:[5, 6]
5:[2, 5]
6:[2, 4]

Status: It's your turn to make a move. Enter your command.
> Hello
Invalid input. Please try again.
>

Example 3

Mid-game example. The "domino snake" exceeds six dominoes in length.

======================================================================
Stock size: 7
Computer pieces: 4

[6, 6][6, 3][3, 0]...[4, 2][2, 3][3, 6]

Your pieces:
1:[0, 0]
2:[1, 2]
3:[5, 5]

Status: It's your turn to make a move. Enter your command.

Example 4

The player wins.

======================================================================
Stock size: 13
Computer pieces: 2

[3, 5][2, 2][6, 6]...[3, 6][0, 3][3, 4]

Your pieces:
1:[4, 4]

Status: It's your turn to make a move. Enter your command.
> 1
======================================================================
Stock size: 13
Computer pieces: 2

[3, 5][2, 2][6, 6]...[0, 3][3, 4][4, 4]

Your pieces:

Status: The game is over. You won!



import itertools
import random
import re

next_player = {
    "pair": [-1, -1],
    "player": ""
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


def is_valid(s):
    is_integer = bool(re.fullmatch(r"[-+]?\d+", s.strip()))
    if not is_integer:
        return False
    # Check if it's a whole number
    try:
        int(s)
        return True
    except ValueError:
        return False


def display_status():
    print("=" * 70)
    print(f"Stock size: {len(stock)}")
    print(f"Computer pieces: {len(computer)}")
    print()
    if len(dominoes) < 6:
        print(*dominoes)
    else:
        print(*dominoes[0:3], "...", *dominoes[-3:], sep="")
    print()
    print(f"Your pieces:")
    for i, piece in enumerate(player):
        print(f"{i + 1}:{piece}")
    print()

def make_move(deck, index):
    item_ = deck.pop(abs(index) - 1)
    if index < 0:
        dominoes.insert(0, item_)
    else:
        dominoes.append(item_)
    return deck


def is_snake_complete():
    """The snake is complete only when the end numbers are identical and the same number appears 8 times in the snake"""
    if len(dominoes) < 6:
        return False

    first_piece = dominoes[0]
    last_piece = dominoes[-1]
    flat_map = []

    ends_meet = first_piece[0] == last_piece[1]

    if ends_meet:
        end = first_piece[0]
        for domino in dominoes:
            flat_map.extend(domino)
        occurences = flat_map.count(end)
        if occurences == 8:
            return True
    return False


def initialize_dominoes():
    global dominoes, computer, stock, next_player, player
    pairs = list(itertools.combinations_with_replacement(range(7), 2))
    pairs = list(map(lambda x: list(x), pairs))

    while next_player['pair'] == [-1, -1]:
        player, computer, stock = allocate_pieces(pairs)
        for (player_pair, computer_pair) in zip(player, computer):
            if is_double(player_pair):
                is_next_player(player_pair, "computer")
            if is_double(computer_pair):
                is_next_player(computer_pair, "player")

    dominoes.append(next_player["pair"])
    if next_player["player"] == "player":
        double_s_index = computer.index(next_player["pair"])
        del computer[double_s_index]
    else:
        double_s_index = player.index(next_player["pair"])
        del player[double_s_index]


def make_computer_move():
    global computer, next_player
    computer_choice = random.choice(range(-len(computer), len(computer)))
    if computer_choice == 0:
        if len(stock) != 0:
            item_ = stock.pop()
            computer.append(item_)
            next_player["player"] = "player"
            return
        else:
            # Skip a turn
            next_player["player"] = "player"
            pass
    else:
        computer = make_move(computer, computer_choice)


initialize_dominoes()
while True:
    display_status()
    if len(player) == 0 or len(computer) == 0:
        print("Status: The game is over. You won!" if len(player) == 0 else "The game is over. The computer won.")
        break
    elif is_snake_complete():
        print("Status: The game is over. It's a draw!")
        break

    if next_player["player"] == "player":
        print("Status: It's your turn to make a move. Enter your command.")
    else:
        print("Status: Computer is about to make a move. Press Enter to continue...")

    while True:
        # Case for the player
        if next_player["player"] == "player":
            player_move = input()
            if not is_valid(player_move):
                print("Invalid input. Please try again.")
                continue
            elif abs(int(player_move)) > len(player):
                print("Invalid input. Please try again.")
                continue

            move = int(player_move)
            if move == 0:
                if len(stock) != 0:
                    item = stock.pop()
                    player.append(item)
                    next_player["player"] = "computer"
                    break
                else:
                    # Skip a turn
                    next_player["player"] = "computer"
                    pass
            else:
                player = make_move(player, move)
                next_player["player"] = "computer"  # Switch the players
                break
            next_player["player"] = "computer"  # Switch the players
        else:
            pressing_enter = input()
            make_computer_move()
            next_player["player"] = "player"
            break


