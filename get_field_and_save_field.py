import requests
import json
import json_controller
import game_methods


def get_field_for_user(name, game_id):
    # Отправляем запрос на getField.
    get_host_field = requests.get(f'http://localhost:8080/game/getField/?name={name}&gameId={game_id}').text

    # Получаем поле с клеточками, кораблями, для расстановки.

    field = json.loads(get_host_field, object_hook=json_controller.JSONObject)
    return  field

# Расставляес корабли
def ships_place(field):
    print(f'Имя игрока: {field.user.name}, его ID: {field.user.id}')
    for i, ship in enumerate(field.ships):
        print(f'Корабль №{i + 1}. ID: {ship.id}')

        # Достаем из запроса field поле для координат корабля и делаем его списком
        field.ships[i].allCells = []

        # ID i-того корабля
        ship_id = field.ships[i].id

        # Проверяем возможность установки корабля
        # потребуется переработать для 3x и 4x палубного корабля!!!
        ship_coord = game_methods.check_ship_coord(ship, field)

        # Начальные и конечные координаты корабля:
        # 1) Начальные
        start_x = int(ship_coord[0][0])
        start_y = int(ship_coord[0][1])
        start_cell = game_methods.get_cell(start_x, start_y, field)
        # 2) Конечные
        end_x = int(ship_coord[1][0])
        end_y = int(ship_coord[1][1])
        end_cell = game_methods.get_cell(end_x, end_y, field)
        # Заполняем allCells
        ship.allCells = [start_cell, end_cell]

    return field

def save_field(field):
    # отправляес на сервер SaveField для игрока
    data = json_controller.to_JSON(field)
    url = 'http://localhost:8080/game/saveField'
    headers = {'Content-type': 'application/json',  # Определение типа данных
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    json_post = requests.post(url, data=data, headers=headers)

    print(f'Ответ: {json_post}')
    print(f'Статус: {json_post}')
    print(f'Текст JSON запроса: {json_post}')
    print(data)


save_field(ships_place(get_field_for_user))

