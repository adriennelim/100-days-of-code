ttt = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]

#Main tic tac toe game
def play_tic_tac_toe ():
    turn = 1
    winner = "No one! It's a tie!"
    while turn < 10:
        print_board()
        player_input(turn)
        if find_winner() == True:
            winner = "Player 1"
            if turn % 2 == 0:
                winner = "Player 2"
            ttt = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
            break
        else:
            turn += 1
    return f'Winner is... {winner}'

#Display board to players
def print_board ():
    print(ttt[0:3])
    print(ttt[3:6])
    print(ttt[6:9])


#Enter user input by turns and replace coordinates on board with player symbol
def player_input (turn):
    p1_symbol = " X "
    p2_symbol = " O "
    player = 1
    if turn % 2 == 0:
        player = 2

    if player == 1:
        user_input = input(f'Player {player} ({p1_symbol}), where will you play? ')
        coordinates = tuple(int(x) for x in user_input.split(","))
        # alternatively, use map: test_tup = tuple(map(int, test.split(",")))
        idx = ttt.index(coordinates)
        ttt[idx] = p1_symbol

    elif player == 2:
        user_input = input(f'Player {player} ({p2_symbol}), where will you play?')
        coordinates = tuple(int(x) for x in user_input.split(","))
        idx = ttt.index(coordinates)
        ttt[idx] = p2_symbol

#find the winning combination
def find_winner():
    outcome = False
    if ttt[0] == ttt[3] == ttt[6]:
        outcome = True
    elif ttt[1] == ttt[4] == ttt[7]:
        outcome = True
    elif ttt[2] == ttt[5] == ttt[8]:
        outcome = True
    elif ttt[0] == ttt[4] == ttt[8]:
        outcome = True
    elif ttt[6] == ttt[4] == ttt[2]:
        outcome = True
    elif ttt[0] == ttt[1] == ttt[2]:
        outcome = True
    elif ttt[3] == ttt[4] == ttt[5]:
        outcome = True
    elif ttt[6] == ttt[7] == ttt[8]:
        outcome = True
    return outcome




