from factory import ChickenFactory, MoldavianChicken, BelarusianChicken, RussianChicken

chickens_dict = {RussianChicken: 50, MoldavianChicken: 30, BelarusianChicken: 25}
factory = ChickenFactory(chickens_dict)


def test_generate_chickens():
    assert factory.generate_chickens() == 'Курицы созданы! Расчеты проведены.'


def test_chicken_count():
    assert factory.chicken_count == 105


def test_eggs_per_month():
    assert factory.eggs_per_month == 2245


'''
 python -m pytest tests/factory_test.py -v
'''
