class Rules():
    """
    Класс правил, получает длинну матрицы game_len(по умолчанию 3)
    Создает вертикальные, горизонтальные и диагональные правила для проверки
    """
    def __init__(self, game_len=3):
        self.game_len = game_len                         #Сохраняем длинну матрицы
        self.rules = [[z for z in range(self.game_len)],] #создаем базовое правило

    def create(self):
        horizontal_rules = self.horizontal_rules(self.rules)
        vertical_rules = self.vertical_rules(horizontal_rules)
        diagonal = self.diagonal_rules(horizontal_rules)
        all_rules = diagonal + vertical_rules + horizontal_rules
        return all_rules

    def horizontal_rules(self, r):
        while len(r) < self.game_len:
            r.append([x+self.game_len for x in r[-1]])
            self.horizontal_rules(r)
        return r

    def vertical_rules(self, arr):
        j = 0
        a = []
        for i in range(self.game_len):
            a.append([y[j] for y in arr])
            j += 1
        return a
    def diagonal_rules(self, arr):
        j = 0
        a = []
        for i in range(self.game_len):
            a.append(arr[i][j])
            j += 1
        j = self.game_len
        l = []
        for i in range(self.game_len):
            l.append(arr[i][j-1])
            j -= 1
        return [a, l]
