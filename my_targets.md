#**Мои задачи:**
####1) добавить в клиент взаимодействие с написанными методами для создания поиска и вступления в игру


#_*MAPPINGS:*_
##Маппинг/ Тип (get/post)/ Принимаемые параметры/ Что возвращает/ Что делает
1. localhost:8080/**hello/init**	get		OK/NOK	Создание всех необходимых таблиц в баще данных

2. localhost:8080/**user/create/?name=X&password=Y**	get	String name, String password	OK/NOK	Занесение в table users 
имя пользователя и пароля пользователя

3. localhost:8080/**user/check/?name=X&password=Y**	get	String name, String password	OK/NOK	Проверка на наличие 
пользователя среди уже зарегистрированных

4. localhost:8080/**game/createRoom/?name=X**	get	String name	OK/NOK	Создает игру(хост)

5. localhost:8080/**game/join/?name=X&id=Y**	get	int id, String name	OK/NOK	Подключает seconduser в лобби к хосту
***X - _имя seconduser_***
***Y - _GAME id_***
 6. localhost:8080/**game/found/**	get		List(game) JSON	Показывает все игры, где есть хосты, но нет secondplayer
 
 
                            ============ 2 ====================
Делаем запрос на сервер, в ответ приходит JSON (все игры, где есть хосты, но нет secondplayer)
то есть список хостов, ожидающих в cвоих комнатах.
lobby_games_request = requests.get(f'http://localhost:8080/game/found')

Приходит JSON объект(str) [{'id':, 'userHost': 'Jony', 'secondUser': None, 'fieldId': 0, 'started': False}, ...]
десериализуем JSON в PY List  ___json.load___ deserialze _file_ and ___json.loads___ deserialize a _string_
active_lobby = json.loads(lobby_games_request.text)


                            ============ 3 ====================
Игрок в Главном меню нажимает "Найти игру" и переходит в лобби (становиться SecondUser),
клиент отправляет раз в _??? 1 сек ???_ . запрос на сервер из Пункта 2. game/found ( лобби обновляется)
SecondUser выбирает свободную команут и нажимает кнопку "Присоедениться"
отправляем на сервер информацию: name - SecondUsername, id - ID комнаты

joiner_name = None  # вносим имя пользователя secondUser
game_id = None      # вносим ID комнаты

join_to_game_request = requests.get(f'http://localhost:8080/game/join/?name={joiner_name}&id={game_id}')
 