import requests
import json

import property
import json_controller
import game_methods

game_id = property.game_id


def game_reques(game_id):
    '''

    :param game_id:
    :return: объекты игры
    '''
    try:
        update_game = property.game_update_game
        payload = {'gameId': game_id}
        update_game_request = requests.get(update_game, params=payload).text
        game_content = json.loads(update_game_request, object_hook=json_controller.JSONObject)
        return game_content
    except:
        print('=> !!!ERROR!!! <=')


def get_game_info():
    game = game_reques(game_id)
    print(f'ID игры: {game.id}')
    print(f'Host игры:')
    print(get_user_info('hostField', game))
    print('===========================')
    print(f'Joiner игры:')
    print(get_user_info('joinField', game))


def get_user_info(user_role, game):
    '''
    :param user_role: либо хост: 'hostField'
                      либо второй игрок: 'joinField'

    :return: инфо об игроке.
    '''

    if user_role == 'hostField':
        user = game.hostField
    if user_role == 'joinField':
        user = game.joinField

    name = user.user.name
    ready_status = user.ready

    return f'Имя: {name}, статус готовности {ready_status}'


def get_boards(user_role, game):
    '''

            :param user_role:
            :param game:
            :return:

    '''
    your_board = game_methods.new_board(4)
    enemy_board = game_methods.new_board(4)

    if user_role == 'hostField':
        myself_board = game_methods.paint_myself_field(your_board, game.hostField)
        enemy_board = game_methods.paint_enemy_field(enemy_board, game.joinField)
        enemy_name = game.joinField.user.name

    if user_role == 'joinField':
        myself_board = game_methods.paint_myself_field(your_board, game.joinField)
        enemy_board = game_methods.paint_enemy_field(enemy_board, game.hostField)
        enemy_name = game.hostField.user.name

    print('==============')
    print('Ваше поле:   ')
    for row in myself_board:
        print(row)

    print('==============')
    print(f'Поле противника {enemy_name}:')
    for row in enemy_board:
        print(row)

    return (myself_board, enemy_board)
