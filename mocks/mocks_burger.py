from unittest.mock import Mock

from helpers import GenerateTestData


class BurgerMocks:
    @staticmethod
    def mock_bun():
        mock_bun = Mock()
        test_data = GenerateTestData()
        name = test_data.random_bun_name()
        price = test_data.random_bun_price()
        mock_bun.get_name.return_value = name
        mock_bun.get_price.return_value = price
        return mock_bun

    @staticmethod
    def mock_ingredient(ingredient_data):
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = ingredient_data[0]
        mock_ingredient.get_name.return_value = ingredient_data[1]
        mock_ingredient.get_price.return_value = ingredient_data[2]
        return mock_ingredient