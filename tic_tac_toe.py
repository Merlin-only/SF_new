board = list(range(1, 10))
win = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def draw_board():
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)


def player_input(symbol):
    while True:
        value = input('В какое поле поставить: ' + symbol + '? ')
        if not (value in '1, 2, 3, 4, 5, 6, 7, 8, 9'):
            print('Ошибка ввода. Укажите корректный номер ячейки')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('Эта ячейка занята, введите другой номер ячейки')
            continue
        board[value - 1] = symbol
        break


def check_win(board):
    for i in win:
        if (board [i[0] - 1]) == (board[i[1] - 1]) == (board[i[2] - 1]):
            return board[i[0] -1]
    return False


def main():
    count = 0
    while True:
        draw_board()
        if count % 2 == 0:
            player_input('X')
        else:
            player_input('O')
        if count > 3:
            winner = check_win(board)
            if winner:
                draw_board()
                print('Победитель игрок ', winner)
                break
        count += 1
        if count == 9:
            draw_board()
            print('Ничья')
            break


main()
