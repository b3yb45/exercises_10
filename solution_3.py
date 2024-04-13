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
    def is_space_occupied(x, y):
        try:
            return NavalBattle.playing_field[y][x] == 1 or \
                   NavalBattle.is_adjacent_space_occupied(x, y) \
                   or not ((0 <= x < 10) and (0 <= y < 10))
        except IndexError:
            return True

    @staticmethod
    def is_adjacent_space_occupied(x, y):
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1),
                        (1, -1), (-1, 1), (-1, -1)):
            #Проверка на выход за пределы игрового поля
            if (0 <= x + dx < 10) and (0 <= y + dy < 10):
                if NavalBattle.playing_field[y + dy][x + dx] == 1:
                    return True
        return False
    
    @staticmethod
    def check_field(x, y, ship_length):
        orients_dict = {"right": True, "up": True, "left": True, "down": True}

        if NavalBattle.is_space_occupied(x, y):
            return []

        for orient in orients_dict:
            for i in range(ship_length):
                try:
                    if NavalBattle.is_space_occupied(x + (i if orient == "right" else 0) - (i if orient == "left" else 0),
                                                        y + (i if orient == "down" else 0) - (i if orient == "up" else 0)):
                        orients_dict[orient] = False
                        break
                except IndexError:
                    orients_dict[orient] = False
                    break

        return [orient for orient, is_possible in orients_dict.items() if is_possible]

    @staticmethod
    def place_ship(x, y, ship_length, orient):
        for i in range(ship_length):
            if orient == "right":
                NavalBattle.playing_field[y][x + i] = 1
            elif orient == "up":
                NavalBattle.playing_field[y - i][x] = 1
            elif orient == "left":
                NavalBattle.playing_field[y][x - i] = 1
            elif orient == "down":
                NavalBattle.playing_field[y + i][x] = 1
        return

    @staticmethod
    def new_game():
        #Create new game
        NavalBattle.playing_field = [[0] * 10 for _ in range(10)]
        ship_quant = 1
        for ship_length in range(4, 0, -1):
            for _ in range(ship_quant):
                orient = ""
                while orient == "":
                    x = random.randint(0, 9)
                    y = random.randint(0, 9)
                    try:
                        orient = random.choice(NavalBattle.check_field(x, y, ship_length))
                    except IndexError:
                        continue
                NavalBattle.place_ship(x, y, ship_length, orient)
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
            return
        else:
            NavalBattle.playing_field[y - 1][x - 1] = "o"
            print("Мимо!")
            return

    @staticmethod
    def show():
        for y in NavalBattle.playing_field:
            for x in y:
                if x == 0 or x == 1:
                    print('~', end=' ')
                else:                 
                    print(f'{x}', end=' ')
            print()


    @staticmethod
    def show_uncovered():
        for y in NavalBattle.playing_field:
            for x in y:
                print(f'{x}', end=' ')
            print()
