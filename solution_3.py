import random


class NavalBattle:
    playing_field = []
    __player_symbols = ["0", "1", "~", "o"]
    
    def __init__(self, symbol):
        if str(symbol) in NavalBattle.__player_symbols or len(str(symbol)) > 1:
            raise ValueError
        
        self.__symbol = str(symbol)
        NavalBattle.__player_symbols.append(self.__symbol)

    @staticmethod
    def check_field(x, y, ship_length):
        right_free = True
        #Check right
        for i in range(ship_length):
            try:
                if NavalBattle.playing_field[y][x + i] == 1:
                    right_free = False
                    break
            except IndexError:
                right_free = False
                break
        
        up_free = True
        #Check up
        for i in range(ship_length):
            try:
                if NavalBattle.playing_field[y - i][x] == 1:
                    up_free = False
                    break
            except IndexError:
                up_free = False
                break

        left_free = True
        #Check left
        for i in range(ship_length):
            try:
                if NavalBattle.playing_field[y][x - i] == 1:
                    left_free = False
                    break
            except IndexError:
                left_free = False
                break

        down_free = True
        #Check down
        for i in range(ship_length):
            try:
                if NavalBattle.playing_field[y + i][x] == 1:
                    down_free = False
                    break
            except IndexError:
                down_free = False
                break
        
        orient_dict = {1: right_free, 2: up_free, 3: left_free, 4: down_free}
        poss_orient = [k for k, v in orient_dict.items() if v]
        return poss_orient

    @staticmethod
    def place_ship(x, y, ship_length, orient):
        if orient == 1:
            for i in range(ship_length):
                NavalBattle.playing_field[y][x + i] = 1
        elif orient == 2:
            for i in range(ship_length):
                NavalBattle.playing_field[y + i][x] = 1
        elif orient == 3:
            for i in range(ship_length):
                NavalBattle.playing_field[y][x - i] = 1
        elif orient == 4:
            for i in range(ship_length):
                NavalBattle.playing_field[y + i][x] = 1
        return

    @staticmethod
    def new_game():
        #Create new game
        NavalBattle.playing_field = [[0] * 10 for _ in range(10)]
        
        for ship_length in range(4, 0, -1):
            ship_quant = 1
            for _ in range(ship_quant):
                orient = []
                while orient == []:
                    x1 = random.randint(0, 9)
                    y1 = random.randint(0, 9)
                    orient = random.choice(NavalBattle.check_field(x1, y1, ship_length))
                NavalBattle.place_ship(x1, y1, ship_length, orient)
            ship_quant += 1

        return

    def shot(self, x, y):
        if not 0 < x < 11 or not 0 < y < 11 or not isinstance(x, int) or not isinstance(y, int):
            raise ValueError

        if NavalBattle.playing_field == []:
            print('Игровое поле не заполнено!')
            return

        if NavalBattle.playing_field[y - 1][x - 1] in NavalBattle.__player_symbols[3:]:
            print('Ошибка!')
            return

        if NavalBattle.playing_field[y - 1][x - 1] == 1:
            NavalBattle.playing_field[y - 1][x - 1] = self.__symbol
            print("Попал!")
        else:
            NavalBattle.playing_field[y - 1][x - 1] = "o"
            print("Мимо!")

    @staticmethod
    def show():
        for y in NavalBattle.playing_field:
            for x in y:
                if x == 0 or x == 1:
                    print('~', end='')
                else:                 
                    print(f'{x}', end='')
            print()
