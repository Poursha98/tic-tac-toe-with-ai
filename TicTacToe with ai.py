board = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}

computer = "X"
player = "O"


def board_print(board):
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("-" * 10)
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("-" * 10)
    print(board[7] + " | " + board[8] + " | " + board[9])
    print("-" * 10)
    print("\n")


def space_ckeck(position):
    if board[position] == " ":
        return True

    return False


def insert_letter(letter, position):
    if space_ckeck(position):
        board[position] = letter
        board_print(board)
        if draw_check():
            print("it's a draw")
            exit()
        if win_check():
            if letter == "X":
                print("Bot wins...")
            else:
                print("You win...")
        return
    else:
        print("this position is full...")
        position = int(input("please chose another :"))
        insert_letter(letter, position)
        return


def win_check():
    if board[1] == board[2] == board[3] and board[1] != " ":
        return True
    elif board[4] == board[5] == board[6] and board[4] != " ":
        return True
    elif board[7] == board[8] == board[9] and board[7] != " ":
        return True
    elif board[1] == board[4] == board[7] and board[1] != " ":
        return True
    elif board[2] == board[4] == board[8] and board[2] != " ":
        return True
    elif board[3] == board[6] == board[9] and board[3] != " ":
        return True
    elif board[1] == board[5] == board[9] and board[1] != " ":
        return True
    elif board[3] == board[5] == board[7] and board[3] != " ":
        return True
    else:
        return False


def draw_check():
    for key in board.keys():
        if board[key] == " ":
            return False
    return True


def check_mark_won(mark):
    if board[1] == board[2] == board[3] and board[1] == mark:
        return True
    elif board[4] == board[5] == board[6] and board[4] == mark:
        return True
    elif board[7] == board[8] == board[9] and board[7] == mark:
        return True
    elif board[1] == board[4] == board[7] and board[1] == mark:
        return True
    elif board[2] == board[4] == board[8] and board[2] == mark:
        return True
    elif board[3] == board[6] == board[9] and board[3] == mark:
        return True
    elif board[1] == board[5] == board[9] and board[1] == mark:
        return True
    elif board[3] == board[5] == board[7] and board[3] == mark:
        return True
    else:
        return False


def player_move():
    position = int(input("Enter a position for 'O' :"))
    insert_letter(player, position)
    return


def computer_move():
    best_score = -800
    best_move = 0
    # navigate potential moves :
    for key in board.keys():
        if board[key] == " ":
            board[key] = computer
            score = minimax(board, False)
            board[key] = " "
            if score > best_score:
                best_score = score
                best_move = key
    insert_letter(computer, best_move)
    return


def minimax(computer, is_maximizing):
    if check_mark_won(computer):
        return 1
    elif check_mark_won(player):
        return -1
    elif draw_check():
        return 0

    if is_maximizing:
        best_score = -800
        for key in board.keys():
            if board[key] == " ":
                board[key] = computer
                score = minimax(board, False)
                board[key] = " "
                if score > best_score:
                    best_score = score
        return best_score

    else:
        best_score = +800
        for key in board.keys():
            if board[key] == " ":
                board[key] = player
                score = minimax(board, True)
                board[key] = " "
                if score < best_score:
                    best_score = score
        return best_score


while not win_check():
    computer_move()
    player_move()
