
# Адрес и порт сервера:
serv_adress = 'http://localhost'
serv_port = 8080

# Запросы:

## user/check
user_check_request = f'{serv_adress}:{serv_port}/user/check'

# user/create
user_create_request = f'{serv_adress}:{serv_port}/user/create'

# game/createRoom
game_create_room = f'{serv_adress}:{serv_port}/game/createRoom'

# game/join
game_join = f'{serv_adress}:{serv_port}/game/join'

# game/found
game_found = f'{serv_adress}:{serv_port}/game/found'

# game/leave
game_leave = f'{serv_adress}:{serv_port}/game/leave'

# game/updateGame
game_update_game = f'{serv_adress}:{serv_port}/game/updateGame'

# play/shoot
play_shoot = f'{serv_adress}:{serv_port}/play/shoot'

# play/turn
play_turn = f'{serv_adress}:{serv_port}/play/turn'


# play/surrender
play_surrender = f'{serv_adress}:{serv_port}/play/surrender'


# Временные параметры для get_field, game_simulation
# ==================================
name_host = 'test1'
name_join = 'test2'
game_id = 9315
# ==================================
