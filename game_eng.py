class Boards:
    def __init__(self):
        self.my_board_part = [[0] * 10 for i in range(10)]
        self.enemy_board_part = [[0] * 10 for i in range(10)]


class Player:
    def __init__(self, name):
        self.name = name
        self.ship_counter = {'4 палубный': 0, '3 палубный': 0, '2 палубный': 0, '1 палубный': 0}
        self.ship_map = Boards()

    def shoot(self, x, y, target):
        """
        функция принимает координаты и цель
        x - строка
        y - столбец
        target - цель, в кого стрельяем
        """
        if target.ship_map.my_board_part[x][y] == 'S': # S- обозначение корабля
            print('Вы попали!')
            target.ship_map.my_board_part[x][y] = 'X'
            self.ship_map.enemy_board_part[x][y] = 'X'
            return True
        else:
            target.ship_map.my_board_part[x][y] = 'M'
            self.ship_map.enemy_board_part[x][y] = 'M'
            print("Мимо!")
            return False


class Game:
    def __init__(self):
        self.p1 = Player('Nick')
        self.p2 = Player('Danny')

    def play_game(self):
        print('Стреляет первый игрок!')
        self.p1.shoot(1, 1, self.p2)
        print('Стреляет второй игрок!')
        self.p2.shoot(2, 2, self.p1)
        print('Стреляет первый игрок!')
        self.p1.shoot(2, 2, self.p2)
        print('Стреляет второй игрок!')
        self.p2.shoot(0, 0, self.p1)
        print('Стреляет первый игрок!')
        self.p1.shoot(4, 4, self.p2)
        print('Стреляет второй игрок!')
        self.p2.shoot(9, 9, self.p1)
        # print('Начнём игру')
        # p1b = self.boards()
        # while self.p1.b


# nick = Player('Nick').ship_map
# print(nick)



# player_1 = Boards()
# player_2 = Boards()
#
# nick.my_board_part[0][5] = 'S'
# nick.my_board_part[1][5] = 'S'
# nick.my_board_part[5][5] = 'S'
# nick.my_board_part[1][5] = 'S'
# nick.my_board_part[2][5] = 'S'
# nick.my_board_part[4][5] = 'S'
#
# for i in nick.my_board_part:
#     print(i)
# print('===================================')
# for i in nick.enemy_board_part:
#     print(i)

round1 = Game()
round1.play_game()

players_1_stack = [round1.p1.ship_map.my_board_part, round1.p1.ship_map.enemy_board_part]
players_2_stack = [round1.p2.ship_map.my_board_part, round1.p2.ship_map.enemy_board_part]
players_stack = [players_1_stack, players_2_stack]

num = 1
for i in players_stack:
    print(f'++++++++  Игрок {num}   ++++==')
    for j in players_stack[num-1]:
        if i.index(j) == 0:
            print('\nТвое поле: \n')
        else:
            print('\nПоле противника: \n')
        for s in j:
            print(s)
    num += 1
    # for j in players_stack[i]:

