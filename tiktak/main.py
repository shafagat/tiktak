from rules import Rules


class Game():
    """
    Класс игры
    метод play реализует игру
    check_rules проверяет заполнение ячеек
    draw_game отрисовывает в консоли игру
    """
    def __init__(self, game_len):
        self.game_len = game_len                                #Сохраняем длинну матрицы
        self.game_matrix = [[' ' for x in range(self.game_len)] for h in range(self.game_len)] #Матрица игры
        self.symbols = {'x': 'Крестики', 'o': 'Нолики'}          #Символы для вывода

    def _validate_symbol(self, symbol):
        if symbol.lower() not in ['x', 'o']:
            raise ValueError('Недопустимый символ')
        return symbol

    def _validate_input(self, val):
        try:
            val = int(val)
        except ValueError:
            raise ValueError('Недопустимый символ')
        if int(val) > self.game_len:
            raise ValueError('Недопустимый символ, число превышает размер игры')
        return val

    def check_rules(self, x, rule, arr):
        status = False
        j = []
        for y in arr:
            for f in y:
                j.append(f)
        for i in rule:
            if j[i] != x:
                return False
        return True

    def play(self):
        a = self._validate_input(input('Введите число строки '))
        b = self._validate_input(input('Введите число столбца '))

        symbol = self._validate_symbol(input('Введите символ '))

        row = int(a) - 1
        column = int(b) - 1
        if self.game_matrix[row][column] == ' ':
            self.game_matrix[row][column] = symbol
        else:
            print('Здесь уже есть символ!')
            return
        j = Rules(self.game_len)
        rules = j.create()
        for r in rules:
            check = self.check_rules(symbol, r, self.game_matrix)
            if check == True:
                print('Поздравляем, {} выиграли!'.format(self.symbols[symbol]))
                return True

    def draw_game(self):
        s = '0'
        for i in range(self.game_len):
            s += ' ' + str(i+1)
        s+= '\n'
        for i in range(self.game_len):
            s += '' + str(i+1)
            for i in range(self.game_len):
                s += ' {}'
            s += '\n'
        j = []
        for y in self.game_matrix:
            for f in y:
                j.append(f)
        s = s.format(*j)
        print(s)

game_len = input('Введите длинну игры(по умолчанию 3) ')
if len(game_len) == 0:
    game_len = 3

game = Game(int(game_len))
for i in range(int(game_len)*int(game_len)):
    game.draw_game()
    status = game.play()
    if status == True:
        break
