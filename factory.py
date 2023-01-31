from chicken import RussianChicken, MoldavianChicken, BelarusianChicken


class ChickenFactory:
    def __init__(self, chickens_dict: dict):
        self.__chicken_objects = chickens_dict
        self.__chickens = None
        self.__chicken_count = 0
        self.__eggs_per_month = 0

    def generate_chickens(self):
        self.__chickens = self.__set_chickens(self.__chicken_objects)
        self.__count_chickens()
        self.__count_monthly_production()
        return 'Курицы созданы! Расчеты проведены.'

    def __set_chickens(self, chicken_objects):
        chickens = list()
        for key in chicken_objects:
            chickens.append(self.__create_chicken_from_type(key, chicken_objects[key]))
        return chickens

    def __count_chickens(self):
        for obj in self.__chickens:
            self.__chicken_count += len(obj)

    def __count_monthly_production(self):
        for obj in self.__chickens:
            self.__eggs_per_month += obj[0].laid_per_month * len(obj)
        return self.__eggs_per_month

    @staticmethod
    def __create_chicken_from_type(chicken_type, count: int):
        chickens = [chicken_type() for i in range(count)]
        return chickens

    @property
    def chickens(self):
        for obj in self.__chickens:
            print(obj[0].hello() + f'\nВсего нас {len(obj)} шт.')
        return self.__chickens

    @property
    def chicken_types(self):
        return self.__chicken_objects

    @property
    def eggs_per_month(self):
        return self.__eggs_per_month

    @property
    def chicken_count(self):
        return self.__chicken_count

    def __repr__(self):
        return f'<Птицефабрика. Производство: {self.__eggs_per_month} яиц в месяц. ' \
               f'Всего {self.__chicken_count} кур>'


if __name__ == '__main__':
    factory = ChickenFactory({RussianChicken: 50, MoldavianChicken: 30, BelarusianChicken: 25})
    print(factory.generate_chickens())
    print(factory.chickens)
    print(factory.chicken_types)
    print(f'В месяц все куры несут {factory.eggs_per_month} яиц. {factory.chicken_count} кур.')
    print(factory)
