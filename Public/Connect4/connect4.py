def init_board(x, y):
    lst = []
    for column in range(x):
        column = []
        for string in range(y):
            column.append(' ')
        lst.append(column)
    return lst


def display_board(board):
    labels = '| 1 | 2 | 3 | 4 | 5 | 6 | 7 |'
    border = '|===|===|===|===|===|===|===|'
    print(labels)
    for column in reversed(range(6)):
        display_string = '| '
        for slot in range(7):
            display_string += board[slot][column]
            display_string += ' | '
        print(border)
        print(display_string)
    print(border)
    print(labels)


def play_move(board, current_piece):
    move = input(
        "In which column would you like to insert your piece? ")
    validate_move(board, move, current_piece)


def validate_move(board, move, current_piece):
    if move.isdigit():
        column = int(move)
        if column > 8 or column < 1:
            print("Please enter a number from 1 to 7")
            play_move(board, current_piece)
        else:
            column -= 1
            validate_column(board, column, current_piece)
    else:
        print("Please enter a number from 1 to 7")
        play_move(board, current_piece)


def validate_column(board, column, current_piece):
    if board[column].count(' ') == 0:
        print("I'm sorry, that column is already full!")
        play_move(board, current_piece)
    else:
        drop_piece(board, column, current_piece)


def drop_piece(board, column, current_piece):
    slot = board[column].index(' ')
    board[column][slot] = current_piece


def check_board_full(board):
    total = 0
    for column in range(7):
        total += board[column].count(' ')
    if total == 0:
        return True
    else:
        return False


def init_vertical_check_lines(board):
    verticals = []
    for column in range(7):
        check_line = ''
        for cell in range(6):
            check_line += board[column][cell]
        verticals.append(check_line)
    return verticals


def init_horizontal_check_lines(board):
    horizontals = []
    for cell in range(6):
        check_line = ''
        for column in range(6):
            check_line += board[column][cell]
        horizontals.append(check_line)
    return horizontals


def init_diagonal_check_lines_right(board):
    coords = [(0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0)]
    right_diagonals = []
    for i in range(6):
        diagonal = ''
        x = coords[i][0]
        y = coords[i][1]
        while x < 7 and y < 6:
            diagonal += board[x][y]
            x += 1
            y += 1
        right_diagonals.append(diagonal)
    return right_diagonals


def init_diagonal_check_lines_left(board):
    coords = [(6, 2), (6, 1), (6, 0), (5, 0), (4, 0), (3, 0)]
    left_diagonals = []
    for i in range(6):
        diagonal = ''
        x = coords[i][0]
        y = coords[i][1]
        while x > -1 and y < 6:
            diagonal += board[x][y]
            x -= 1
            y += 1
        left_diagonals.append(diagonal)
    return left_diagonals


def init_game_state(board, check_lines):
    check_lines.append(init_horizontal_check_lines(board))
    check_lines.append(init_vertical_check_lines(board))
    check_lines.append(init_diagonal_check_lines_right(board))
    check_lines.append(init_diagonal_check_lines_left(board))
    return check_lines


def check_win(board, current_piece):
    target_string = current_piece * 4
    check_lines = []
    check_lines = init_game_state(board, check_lines)
    win = check_string(check_lines, target_string)
    return win


def check_string(check_lines, target_string):
    win = ''
    for group in range(4):
        for line in range(len(check_lines[group])):
            check_line = check_lines[group][line]
            if target_string in check_line:
                win = target_string
                return win
            else:
                if group == 3 and line == (len(check_lines[group])-1):
                    win = 'no'
                    return win



def check_game_over(board, current_piece):
    win = check_win(board, current_piece)
    if win == 'no':
        if not check_board_full(board):
            return 'no'
        else:
            return 'tie'
    elif win == 'XXXX':
        return 'X'
    elif win == 'OOOO':
        return 'O'


def swap_turn(piece):
    if piece == 'X':
        piece = 'O'
    else:
        piece = 'X'
    return piece


def game_loop():
    print("Welcome to my Connect Four clone!")
    player_x = (input("Who will be player X? ") or "Player X")
    player_o = (input("Who will be player O? ") or "Player O")
    print("Let's begin!")

    current_piece = 'X'
    current_player = player_x
    game_board = (init_board(7, 6))
    game_over = 'no'

    while game_over == 'no':
        print()
        display_board(game_board)
        print(f"It's {current_player}'s turn, playing {current_piece}")
        play_move(game_board, current_piece)
        game_over = check_game_over(game_board, current_piece)
        current_piece = swap_turn(current_piece)
        if current_piece == 'X':
            current_player = player_x
        else:
            current_player = player_o

    if game_over == 'X':
        print(f"{player_x} wins! Congratulations!")
    elif game_over == 'O':
        print(f"{player_o} wins! Congratulations!")


game_loop()
