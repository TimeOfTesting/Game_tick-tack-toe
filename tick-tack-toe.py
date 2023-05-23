def greet():
    print('_' * 21)
    print("  Приветствуем Вас   ")
    print("      в игре         ")
    print("  крестики - нолики  ")
    print("  формат ввода: х у  ")
    print("  х - номер строки   ")
    print("  у - номер столбца  ")
    print('_' * 21)
    print()

def playing_field():
    print('  | 0 | 1 | 2 | ')
    print('-' * 15)
    for i, j in enumerate(field):
        line = f'{i} | {" | ".join(map(str, j))} | '
        print(line)
        print('-' * 15)
    print()

def ask():
    while True:
        move = input('      Ваш ход: ').split()
        if len(move) != 2:
            print('Введите две координаты!')
            continue

        x, y = move

        if not(x.isdigit()) or not(y.isdigit()):
            print('Введите числа!')
            continue

        if 0 > int(x) or int(x) > 2 or 0 > int(y) or int(y) > 2:
            print('Введенные координаты находятся вне диапозона! ')
            continue

        if field[int(x)][int(y)] != ' ':
            print('Данная клетка занята! ')
            continue

        return int(x), int(y)

def check_win():
    result_win = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                  ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                  ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for result in result_win:
        num = []
        for i in result:
            num.append(field[i[0]][i[1]])

        if num == ['X', 'X', 'X']:
            print('Выйграл крестик!')
            return True
        if num == ['0', '0', '0']:
            print('Выйграл нолик!')
            return True
    return False


greet()
field = [[' '] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    playing_field()
    if count % 2 != 0:
        print('Ходит крестик!')
    else:
        print('Ходит нолик!')

    x, y = ask()

    if count % 2 != 0:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'

    if check_win():
        break

    if count == 9:
        print('Ничья!')
        break
