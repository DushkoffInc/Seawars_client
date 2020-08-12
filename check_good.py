ships = {'ship1': {'start': (), 'end': ()}, 'ship2': {'start': (), 'end': ()}}

for i, ship in enumerate(ships, 1):
    ship_orient = None
    ship_size = 2
    print(f'{ship}')
    while True:
        try:
            x_start, y_start = input(f'Начальные координаты корабля {ship}:  ').split()

            if int(x_start) > 4 or int(y_start) > 4:
                print('Нельзя выходить за границы поля!')
                print('Попробуйте ещё раз!')
                continue

            else:
                while True:
                    try:
                        x_end, y_end = input(f'Конечные координаты корабля {ship}:  ').split()

                        if int(x_end) > 4 or int(y_end) > 4:
                            print('Нельзя выходить за границы поля!')
                            print('Попробуйте ещё раз!')
                            continue

                        else:
                            break

                    except Exception as ex:
                        print("----------")
                        print(f'Введите координаты через пробел!')
                        print(f'Ошибка:  {ex}')
                        print("----------")
            diff_x = abs(int(x_start) - int(x_end))
            print('Разница по X: ', diff_x)
            diff_y = abs(int(y_start) - int(y_end))
            print('Разница по Y: ', diff_y)

            if diff_x > (ship_size-1) or diff_y > (ship_size-1):
                print(f'Ваш корабль имеет размерность: {ship_size}')
                print(f'Укажите другие координаты')
                continue

            ships[ship]['start'] = (x_start, y_start)
            ships[ship]['end'] = (x_end, y_end)
            print('GOOD!')
            break
        except Exception as ex:
            print("----------")
            print(f'Введите координаты через пробел!')
            print(f'Ошибка:  {ex}')
            print("----------")


print(ships)
