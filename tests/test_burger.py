import pytest

from helpers import GenerateTestData
from mocks.mocks_burger import BurgerMocks
from tests.data import Data


class TestBurger:

    data_generator = GenerateTestData()

    def test_set_mock_bun_expected_values(self, burger):
        bun = BurgerMocks.mock_bun()
        burger.set_buns(bun)

        assert burger.bun == bun

    # В тестах используется два набора параметров для двух типов ингредиентов (соусы, начинки)
    @pytest.mark.parametrize('ingredient_data',
                             [data_generator.generate_ingredient_data_sause(),
                              data_generator.generate_ingredient_data_filling()])
    def test_add_ingredient_one_ingredient(self, ingredient_data, burger):
        ingredient = BurgerMocks.mock_ingredient(ingredient_data)
        burger.add_ingredient(ingredient)

        assert len(burger.ingredients) == 1

    @pytest.mark.parametrize('ingredient_data',
                             [data_generator.generate_ingredient_data_sause(),
                              data_generator.generate_ingredient_data_filling()])
    def test_remove_ingredient_one_ingredient_add_and_one_remove(self, ingredient_data, burger):
        ingredient = BurgerMocks.mock_ingredient(ingredient_data)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_move_ingredient_two_ingredients(self, burger):
        ingredient_data_1 = self.data_generator.random_ingredient()
        ingredient_data_2 = self.data_generator.random_ingredient()
        ingredient_1 = BurgerMocks.mock_ingredient(ingredient_data_1)
        ingredient_2 = BurgerMocks.mock_ingredient(ingredient_data_2)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(1, 0)

        assert burger.ingredients == [ingredient_2, ingredient_1]

    # Проверка получения цены бургера с разным количеством ингридиентов
    @pytest.mark.parametrize('ingredients_number',
                             Data.ingredients_number)
    def test_get_price_one_to_five_ingredients(self, burger, ingredients_number):
        expected_price = 0
        bun = BurgerMocks.mock_bun()
        burger.set_buns(bun)
        expected_price = bun.get_price() * 2
        for i in range(ingredients_number):
            ingredient_data = self.data_generator.random_ingredient()
            ingredient = BurgerMocks.mock_ingredient(ingredient_data)
            burger.add_ingredient(ingredient)
            expected_price += ingredient.get_price()

        assert burger.get_price() == expected_price

    def test_get_receipt_three_ingredients(self, burger):
        #Создаем бургер с тремя ингридиентами
        bun = BurgerMocks.mock_bun()
        burger.set_buns(bun)
        for i in range(3):
            ingredient_data = self.data_generator.random_ingredient()
            ingredient = BurgerMocks.mock_ingredient(ingredient_data)
            burger.add_ingredient(ingredient)
        # Создаем ожидаемый чек
        expected_receipt = []
        expected_receipt.append(f'(==== {bun.get_name()} ====)\n')
        for ingredient in burger.ingredients:
            expected_receipt.append(f'= {str(ingredient.get_type()).lower()} {ingredient.get_name()} =\n')
        expected_receipt.append(f'(==== {bun.get_name()} ====)\n')
        expected_receipt.append(f'\n')
        expected_receipt.append(f'Price: {burger.get_price()}')
        expected_receipt_str = ''.join(expected_receipt)

        assert burger.get_receipt() == expected_receipt_str







