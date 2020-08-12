class Fields:
    field_size = 4

    def __init__(self):
        self.my_board_part = [[0] * self.field_size for i in range(self.field_size)]
        self.enemy_board_part = [[0] * self.field_size for i in range(self.field_size)]


class Player:
    def __init__(self, name):
        self.name = name
        self.ship_map = Fields()

    def repaint_fields(self):
        # поле противника
        for cell in self.ship_map.enemy_board_part:
            print(cell)

# class Cell:
#     def __init__(self, x, y, id):
#         self.x = x
#         self.y = y
#         self.id = id
#         self.status = None
#         # print(f'ID:{self.id},x: {x}, y: {y}')
#
#     def get_coord(self):
#         # return f'ID:{self.id},x: {self.x}, y: {self.y}'
#         return f'ID:{self.id}'


class Ship:
    def __init__(self, id=None, size=2):
        self.start = None
        self.end = None
        self.id = id
        self.size = size

    def get_coordinat(self):
        '''
        Производит проверку корректности координат для корабля
        Функция возвращает << координаты корабля введенных пользователем.
        '''

        while True:
            x_start, y_start = input(f'Начальные координаты корабля {self.id}:  ').split()
            if 0 < int(x_start) > 4 or 0 < int(y_start) > 4:
                print('Нельзя выходить за границы поля!')
                print('Попробуйте ещё раз!')
                continue
            while True:
                x_end, y_end = input(f'Конечные координаты корабля {self.id}:  ').split()

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

            if diff_x > (self.size - 1) or diff_y > (self.size - 1):
                print(f'Ваш корабль имеет размерность: {self.size}')
                print(f'Укажите другие координаты')
                continue
            else:
                self.start = (x_start, y_start)
                self.end = (x_end, y_end)
                # print(f'ship ID:{self.id} poin1:{self.start}, point2:{self.end}')
                break
        res = [self.start, self.end]
        return res

    def check_ships_location(self):
        '''
        Функция:
            -принимает координаты корабля и проверяет возможность расположения его на игровом поле
            -возвращает OK или NOK:
                        - OK, если корапбль не граничит с другими
                        - NOK. игрок пытается поставить корабль рядом с другим в недопустимом диапазоне
        '''

        # if ship_coordin ==
        return "OK"

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


if __name__ == '__main__':
    nik = Player('Nik')
    # перерисовать координаты поля противника
    nik.repaint_fields()
    nik.ship_map.enemy_board_part[0][0] = 's'
    nik.ship_map.enemy_board_part[0][1] = 's'
    print('-----------')
    nik.repaint_fields()