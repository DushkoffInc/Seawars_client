def new_board(board_size):
    board = [['o'] * board_size
             for i in range
             (1, board_size + 1)]
    print('Создана новая доска для игры')
    return board


def paint_myself_field(board, field):
    '''

            Привязка координат кораблся к полю, для отрисовки результата.
            '.' - мимо
            's' - корабль
            '0' - не проверенная клеточка
            'x' - попал, но не убил. Реализация после метода Shoot.

    '''

    for x in range(1, 5):
        for y in range(1, 5):
            cell = get_cell(x, y, field)
            if (cell.checked is False) and (cell.status is None):
                continue
            if cell.status is None:
                board[y - 1][x - 1] = '.'  # мимо
                continue
            board[y - 1][x - 1] = 's'
    return board


def paint_enemy_field(board, field):
    '''

            Привязка координат кораблся к полю, для отрисовки результата.
            '.' - мимо
            '0' - не проверенная клеточка
            'x' - попал, но не убил. Реализация после метода Shoot.

    '''
    # !!! пока просто отрисовка пустого поля !!!
    # после добавления shoot - нужно делать запрос и получить ответы: ы
    # - попал
    # - мимо
    # - убил

    return board


def available_for_ship_marker(cell, field):
    '''
    Функция проходит по клеточкам вокруг заданной клетки
    и присваивает availableForShip - False
    :param cell:
    :return:
    '''
    x = cell.x
    y = cell.y

    try:
        c = get_cell_number(int(x), int(y - 1), field)
        field.cells[int(c)].availableForShip = False
        print(f'{field.cells[c].id}')
    except Exception as ex:
        print(f' 1 SKIP!!!,   {ex}')
    try:
        c = get_cell_number(int(x), int(y + 1), field)
        field.cells[int(c)].availableForShip = False
        print(f'{field.cells[c].id}')
    except Exception as ex:
        print(f' 2 SKIP!!!,   {ex}')

    try:
        c = get_cell_number(int(x - 1), int(y - 1), field)
        field.cells[int(c)].availableForShip = False
        print(f'{field.cells[c].id}')
    except Exception as ex:
        print(f' 3 SKIP!!!,   {ex}')
    try:
        c = get_cell_number(int(x - 1), int(y), field)
        field.cells[int(c)].availableForShip = False
        print(f'{field.cells[c].id}')
    except Exception as ex:
        print(f'4 SKIP!!!,   {ex}')
    try:
        c = get_cell_number(int(x - 1), int(y + 1), field)
        field.cells[int(c)].availableForShip = False
        print(f'{field.cells[c].id}')
    except Exception as ex:
        print(f'5 SKIP!!!,   {ex}')

    try:
        c = get_cell_number(int(x + 1), int(y - 1), field)
        field.cells[int(c)].availableForShip = False
        print(f'{field.cells[c].id}')
    except Exception as ex:
        print(f'SKIP!!!,   {ex}')
    try:
        c = get_cell_number(int(x + 1), int(y), field)
        field.cells[int(c)].availableForShip = False
        print(f'{field.cells[c].id}')
    except Exception as ex:
        print(f'SKIP!!!,   {ex}')
    try:
        c = get_cell_number(int(x + 1), int(y + 1), field)
        field.cells[int(c)].availableForShip = False
        print(f'{field.cells[c].id}')
    except Exception as ex:
        print(f'SKIP!!!,   {ex}')


def get_cell(x, y, field):
    '''
            Функция возвращает нужную клетку из Field
    '''

    for cell in field.cells:
        if cell.x == x and cell.y == y:
            return cell


def get_cell_number(x, y, field):
    for i, cell in enumerate(field.cells):
        if cell.x == x and cell.y == y:
            return i


def check_cell(checked_cell):
    '''
          :param check_cell:

             Функция проверяет клетку на валидность.
             Проверка статуса клеточки, на наличие там частей другого корабля.
             Проверка клеточки на avalibleForShip

          :return:
    '''
    if checked_cell.status is not None:
        print('СТАТУС КЛЕТКИ:')
        print(f"{checked_cell.status}")
        print('Тут уже есть корабль!')
        return 'NOK'
    if checked_cell.availableForShip is False:
        print('Сюда нельзя ставить корабль!')
        return 'NOK'
    print('============================')
    print('Клеточка валидна!')
    print(f'ID клетки: {checked_cell.id}')
    print(f'status клетки: {checked_cell.status}')
    print(f'avalibleForShip: {checked_cell.availableForShip}')
    print('============================')
    return 'OK'


def check_ship_coord(ship, field):
    '''
    Производит проверку корректности координат для корабля
    Функция возвращает << координаты корабля введенных пользователем.
    '''
    if ship.numberOfCells > 1:
        while True:
            try:
                x_start, y_start = input(f'Начальные координаты корабля {ship.id}:  ').split()
                if 0 < int(x_start) > 4 or 0 < int(y_start) > 4:
                    print('Нельзя выходить за границы поля!')
                    print('Попробуйте ещё раз!')
                    continue
                if check_cell(get_cell(int(x_start), int(y_start), field)) == 'NOK':
                    print(f'Тут уже есть корабль! ')
                    continue

                while True:
                    try:
                        x_end, y_end = input(f'Конечные координаты корабля {ship.id}:  ').split()
                        if 0 < int(x_end) > 4 or 0 < int(y_end) > 4:
                            print('Нельзя выходить за границы поля!')
                            print('Попробуйте ещё раз!')
                            continue
                        if check_cell(get_cell(int(x_end), int(y_end), field)) == 'NOK':
                            print(f'Тут уже есть корабль! ')
                            continue
                        else:
                            break
                    except Exception as ex:
                        print("----------")
                        print(f'Введите координаты через пробел!')
                        print(f'Ошибка:  {ex}')
                        print("----------")

                diff_x = abs(int(x_start) - int(x_end))
                # print('Разница по X: ', diff_x)
                diff_y = abs(int(y_start) - int(y_end))
                # print('Разница по Y: ', diff_y)

                if diff_x == 1 and diff_y == 1:
                    print('')
                    print('Нельзя распологать корабли по диагонали xDD')  # для 3x и 4x палубника пересмотреть !
                    continue

                if diff_x == 0 and diff_y == 0:
                    print('')
                    print('Нельзя указывать в координаты одинаковые клетки!')
                    continue

                if diff_x > (ship.numberOfCells - 1) or diff_y > (ship.numberOfCells - 1):
                    print(f'Ваш корабль имеет размерность: {ship.numberOfCells}')
                    print(f'Укажите другие координаты')
                    continue
                else:
                    start = (x_start, y_start)
                    end = (x_end, y_end)
                    print(f'ship ID:{ship.id} >>> Start: {start} <<<,'
                          f' >>> End: {end} <<<')

                    # Назначаем клеткам начала и конца корабля стутус  клетки

                    point_start = get_cell(int(x_start), int(y_start), field)
                    point_start.status = ship.id
                    print(f'!!!!   Клетка начала: {point_start.id} x:{point_start.x}, y:{point_start.y}!!!!!')
                    point_end = get_cell(int(x_end), int(y_end), field)

                    point_end.status = ship.id
                    print(f'!!!!   Клетка Конца: {point_end.id} x:{point_end.x}, y:{point_end.y}!!!!!')


                    # Отмечаем availableForShip - False вокруг клеточек корабля

                    available_for_ship_marker(point_start, field)
                    available_for_ship_marker(point_end, field)


                    return (start, end)

            except Exception as ex:
                print("----------")
                print(f'Введите координаты через пробел!')
                print(f'Ошибка:  {ex}')
                print("----------")
