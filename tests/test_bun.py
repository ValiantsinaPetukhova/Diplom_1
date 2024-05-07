from helpers import GenerateTestData
from praktikum.bun import Bun


class TestBun:
    # Проверка создания экземпляра булки
    def test_bun_creation_expected_values(self):
        test_data = GenerateTestData()
        name = test_data.random_bun_name()
        price = test_data.random_bun_price()
        bun = Bun(name, price)

        assert bun.get_name() == name and bun.get_price() == price

    # Проверка метода получения имени булки
    def test_get_name_expected_value(self):
        test_data = GenerateTestData()
        name = test_data.random_bun_name()
        bun = Bun(name, None)

        assert bun.get_name() == name

    def test_get_price_positive_value(self):
        test_data = GenerateTestData()
        price = test_data.random_bun_price()
        bun = Bun(None, price)

        assert bun.get_price() == price

    def test_get_price_negative_value(self):
        test_data = GenerateTestData()
        price = test_data.random_bun_price_negative()
        bun = Bun(None, price)

        assert bun.get_price() == price
