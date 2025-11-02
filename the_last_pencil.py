from random import choice

players = ('John', 'Jack')

def check_pencils_validity(pencils):
    if not pencils.isnumeric():
        print("The number of pencils should be numeric")
        return False
    elif int(pencils) == 0:
        print("The number of pencils should be positive")
        return False
    else:
        return True

print("How many pencils would you like to use:")
while True:
    pencils = input()
    if check_pencils_validity(pencils):
        pencils = int(pencils)
        break

print(f"Who will be the first ({', '.join(players)}):")
# Decide on who is the bot and who is the human
while True:
    first_player = input()
    if first_player not in players:
        print(f"Choose between {' and '.join(players)}")
    else:
        # The first_player chosen is between the names
        # Jack is always the bot, John is always the human
        bot = 'Jack'
        human = 'John'
        current_player = first_player
        break

def constraint_pencil_inputs():
    while True:
        number = input()
        if number not in ("1", "2", "3"):
            print("Possible values: '1', '2' or '3'")
            continue
        elif int(number) > pencils:
            print("Too many pencils were taken")
            continue
        else:
            return int(number)

def get_bot_move(pencils):
    if pencils % 4 == 0:
        return 3
    elif pencils % 4 == 3:
        return 2
    elif pencils % 4 == 2:
        return 1
    else:  # Losing position (pencils % 4 == 1)
        return choice([i for i in range(1, min(4, pencils + 1))])

# Game loop
while pencils > 0:
    print('|' * pencils)
    print(f"{current_player}'s turn:")
    
    if current_player == bot:
        # Bot's turn
        bot_choice = get_bot_move(pencils)
        print(bot_choice)
        pencils -= bot_choice
    else:
        # Human's turn
        user_choice = constraint_pencil_inputs()
        pencils -= user_choice
    
    # Check if game is over
    if pencils == 0:
        # Current player took the last pencil and loses
        winner = human if current_player == bot else bot
        print(f"{winner} won!")
        break
    
    # Switch players
    current_player = bot if current_player == human else human
