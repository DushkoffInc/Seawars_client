import game_methods as gm
import property as prop
import updateGame as upG
import requests
import time
def shoot_host(x, y):
    '''

    NOK - выстер в проверенную клетку
    MISS - выстрел в клетку, где нет корабля
    RANIL - корабль подбит
    UBIL - корабль потоплен Finish - игрок потопил все коробли противника

    :param x, y:
    :return:
    '''
    field = upG.game_reques(prop.game_id).joinField
    cell_id = gm.get_cell(x, y, field).id
    try:
        shoot_request = prop.play_shoot
        payload = {'cellId': cell_id}
        r = requests.get(shoot_request, params=payload)
        if r.status_code == 200:
            if r.text == 'NOK':
                print('Выстер в проверенную клетку!')
            elif r.text == 'MISS':
                print('Промазал!')
            elif r.text == 'RANIL':
                print('Ранил!')
            else:
                print('Убил!')
    except:
        print('UPS.')


def shoot_join(x, y):
    '''

    NOK - выстер в проверенную клетку
    MISS - выстрел в клетку, где нет корабля
    RANIL - корабль подбит
    UBIL - корабль потоплен Finish - игрок потопил все коробли противника
    Finish - игрок потопил все коробли противника
    :param x, y:
    :return:
    '''
    field = upG.game_reques(prop.game_id).hostField
    cell_id = gm.get_cell(x, y, field).id
    try:
        shoot_request = prop.play_shoot
        payload = {'cellId': cell_id}
        r = requests.get(shoot_request, params=payload)
        if r.status_code == 200:
            if r.text == 'NOK':
                print('Выстер в проверенную клетку!')
            elif r.text == 'MISS':
                print('Промазал!')
            elif r.text == 'RANIL':
                print('Ранил!')
            elif r.text == 'Finish':
                print('Ты потопил все корабли, победа!')
            else:
                print('Убил!')
    except:
        print('UPS.')


def check_possibility_of_turn():
    '''

    LOSE - поражение в игре, окончание игры
    NOK - ожидание хода
    ОК - можно ходить переход в выстрелу
    :return:
    '''
    try:
        check_request = prop.play_turn
        player_name = prop.name_host
        game_id = prop.game_id
        payload = {'playerName': player_name , 'gameId': game_id}
        r = requests.get(check_request, params=payload)
        if r.status_code == 200:
            if r.text == 'NOK':
                print('Ожидайте хода!')
                return 'NOK'
            elif r.text == 'OK':
                print('Можно ходить!')
            else:
                print('Поражение!')
                return 'LOOSE'
    except:
        print(f'Ожидание подключения к серверу...')





def game_shoot():

    while True:
        if check_possibility_of_turn() == 'NOK':
            print('Ожидайте хода')
            time.sleep(1)
            continue
        elif check_possibility_of_turn() == 'LOOSE':
            print('Ты проиграл!')
            return False

        while True:

            try:
                x, y = input(f'Задайте координаты выстрела:  ').split()
                if 0 < int(x) > 4 or 0 < int(y) > 4:
                    print('Нельзя выходить за границы поля!')
                    print('Попробуйте ещё раз!')
                    continue

                shoot_host(x, y)
                break
            except Exception as ex:
                print("----------")
                print(f'Введите координаты через пробел!')
                print(f'Ошибка:  {ex}')
                print("----------")

print(check_possibility_of_turn())








