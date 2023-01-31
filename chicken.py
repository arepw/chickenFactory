class Chicken:
    def __init__(self, laid_per_month: int):
        self.laid_per_month = laid_per_month

    def how_much_laid(self):
        return self.laid_per_month

    def hello(self):
        return 'Я курица! '

    def __repr__(self):
        return f'<{self.hello()}>'


class RussianChicken(Chicken):
    def __init__(self, laid_per_month: int = 23):
        super().__init__(laid_per_month)
        self.origin = 'Россия'

    def hello(self):
        return Chicken.hello(self) + f'Моя страна - {self.origin}. Я несу {self.how_much_laid()} яиц в месяц'


class MoldavianChicken(Chicken):
    def __init__(self, laid_per_month: int = 19):
        super().__init__(laid_per_month)
        self.origin = 'Молдавия'

    def hello(self):
        return Chicken.hello(self) + f'Моя страна - {self.origin}. Я несу {self.how_much_laid()} яиц в месяц'


class BelarusianChicken(Chicken):
    def __init__(self, laid_per_month: int = 21):
        super().__init__(laid_per_month)
        self.origin = 'Беларусь'

    def hello(self):
        return Chicken.hello(self) + f'Моя страна - {self.origin}. Я несу {self.how_much_laid()} яиц в месяц'
