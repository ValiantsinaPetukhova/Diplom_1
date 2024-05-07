import pytest

from praktikum.ingredient import Ingredient
from helpers import GenerateTestData
from tests.data import Data


class TestIngredient:
    test_data = GenerateTestData()

    def test_get_price_expected(self):
        ingredient_price = self.test_data.random_ingredient()[2]
        ingredient = Ingredient(None, None, ingredient_price)

        assert ingredient.get_price() == ingredient_price

    def test_get_name_expected(self):
        ingredient_name = self.test_data.random_ingredient()[1]
        ingredient = Ingredient(None, ingredient_name, None)

        assert ingredient.get_name() == ingredient_name

    @pytest.mark.parametrize('type', Data.ingredient_type)
    def test_get_type_two_types(self, type):
        ingredient = Ingredient(type, None, None)

        assert ingredient.get_type() == type
