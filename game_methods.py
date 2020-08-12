import requests
import json
import json_controller

# for i, ship in enumerate(ships, 1):
#     ship_size = 2
#     print(f'{ship}')
#     while True:
#         try:
#             x_start, y_start = input(f'Начальные координаты корабля {ship}:  ').split()
#
#             if 0 < int(x_start) > 4 or 0 < int(y_start) > 4:
#                 print('Нельзя выходить за границы поля!')
#                 print('Попробуйте ещё раз!')
#                 continue
#
#             else:
#                 while True:
#                     try:
#                         x_end, y_end = input(f'Конечные координаты корабля {ship}:  ').split()
#
#                         if 0 < int(x_end) > 4 or 0 < int(y_end) > 4:
#                             print('Нельзя выходить за границы поля!')
#                             print('Попробуйте ещё раз!')
#                             continue
#
#                         else:
#                             break
#
#                     except Exception as ex:
#                         print("----------")
#                         print(f'Введите координаты через пробел!')
#                         print(f'Ошибка:  {ex}')
#                         print("----------")
#             diff_x = abs(int(x_start) - int(x_end))
#             print('Разница по X: ', diff_x)
#             diff_y = abs(int(y_start) - int(y_end))
#             print('Разница по Y: ', diff_y)
#
#
#             if diff_x == 1 and diff_y == 1:
#                 print('')
#                 print('Нельзя распологать корабли по диагонали xDD')
#                 continue
#
#             if diff_x == 0 and diff_y == 0:
#                 print('')
#                 print('Нельзя указывать в координаты одинаковые клетки!')
#                 continue
#
#             if diff_x > (ship_size-1) or diff_y > (ship_size-1):
#                 print(f'Ваш корабль имеет размерность: {ship_size}')
#                 print(f'Укажите другие координаты')
#                 continue
#
#             else:
#                 ships[ship]['start'] = (x_start, y_start)
#                 ships[ship]['end'] = (x_end, y_end)
#
#             check_elem = None
#             for i, s in enumerate(ships):
#                 print('Проверка ДРУГ НА ДРУГА')
#                 if ships[s] == check_elem:
#                     print('Ащщщщщ, нельзя так!!!')
#                     continue
#                 check_elem = ships[s]
#                 print('GOOD!')
#             break
#         except Exception as ex:
#             print("----------")
#             print(f'Введите координаты через пробел!')
#             print(f'Ошибка:  {ex}')
#             print("----------")


def check_ship_coord(ship):
    '''
    Производит проверку корректности координат для корабля
    Функция возвращает << координаты корабля введенных пользователем.
    '''
    if ship.numberOfCells > 1:
        while True:
            x_start, y_start = input(f'Начальные координаты корабля {ship.id}:  ').split()
            if 0 < int(x_start) > 4 or 0 < int(y_start) > 4:
                print('Нельзя выходить за границы поля!')
                print('Попробуйте ещё раз!')
                continue

            while True:
                x_end, y_end = input(f'Начальные координаты корабля {ship.id}:  ').split()
                if 0 < int(x_end) > 4 or 0 < int(y_end) > 4:
                    print('Нельзя выходить за границы поля!')
                    print('Попробуйте ещё раз!')
                    continue
                else:
                    break

            diff_x = abs(int(x_start) - int(x_end))
            # print('Разница по X: ', diff_x)
            diff_y = abs(int(y_start) - int(y_end))
            # print('Разница по Y: ', diff_y)

            if diff_x == 1 and diff_y == 1:
                print('')
                print('Нельзя распологать корабли по диагонали xDD')
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
                print(f'ship ID:{ship.id} poin1:{start}, point2:{end}')
                break
        print(f'Координаты начальной точки корабля: {start}')
        print(f'Координаты конечной точки корабля: {end}')
        return (start, end)


def check_ships_neighbour(ship_coord):
    '''
    Функция:
        -принимает координаты корабля и проверяет возможность расположения его на игровом поле
        -возвращает OK или NOK:
                    - OK, если корапбль не граничит с другими
                    - NOK. игрок пытается поставить корабль рядом с другим в недопустимом диапазоне
    '''

    # if ship_coordin ==
    return "OK"

def check_cell(cell, field):
    '''Функция проверяет клетку на валидность'''

    for item, c in enumerate(field.cells):
        pass



# поле user_host
name = 'dima'
game_id = 3064

get_host_field = requests.get(f'http://localhost:8080/game/getField/?name={name}&gameId={game_id}').text
hosts_field = json.loads(get_host_field, object_hook=json_controller.JSONObject)

print(f'Имя игрока: {hosts_field.user.name}')

for i, ship in enumerate(hosts_field.ships):
    print(f'Корабль №{i+1}. ID: {ship.id}')
    ship.allCells = []
    print(f'AllCells: {ship.allCells}')
    # Достаем из запроса поле allCells коорабля
    ship = hosts_field.ships[i].allCells
    # ID корабля
    ship_id = hosts_field.ships[i].id

    # проверяем возможность расстановки корабля
    while True:
        ship_coordin = check_ship_coord(hosts_field.ships[i])
        check_ships_neighbour(ship_coordin)

        # Начальные и конечные координаты корабля:
        # 1) Начальные
        start_x_point_ship = int(ship_coordin[0][0])
        start_y_point_ship = int(ship_coordin[0][1])

        # 2) Конечные
        end_x_point_ship = int(ship_coordin[1][0])
        end_y_point_ship = int(ship_coordin[1][1])
        # Добавляем в поле allCells координаты расположения корабля
        # и присваиваем статусы клеткам, которые занимает этот корабль,
        # чекаем, занятые уже клетки

        for j, c in enumerate(hosts_field.cells):
            if int(c.x) == int(start_x_point_ship) and int(c.y) == int(start_x_point_ship):
                ship.append(c)
                c.status = ship_id
            if int(c.x) == int(end_x_point_ship) and int(c.y) == int(end_x_point_ship):
                ship.append(c)
                c.status = ship_id

        break

print(hosts_field.ships[0].allCells[0].id)
