class NavalBattle:
    playing_field = [[0] * 10 for _ in range(10)]
    __player_symbols = ["0", "1", "o", "~"]

    def __init__(self, symbol):
        if str(symbol) in NavalBattle.__player_symbols or len(str(symbol)) > 1:
            raise ValueError
        
        self.__symbol = str(symbol)
        NavalBattle.__player_symbols.append(self.__symbol)

    def shot(self, x, y):
        if not 0 < x < 11 or not 0 < y < 11 or not isinstance(x, int) or not isinstance(y, int):
            raise ValueError
        
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
