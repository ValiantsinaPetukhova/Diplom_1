import random

from praktikum.ingredient_types import *
from tests.data import Data


class GenerateTestData:
    def random_bun_name(self):
        data = Data()
        random_bun_name = random.choice(data.bun_name)
        return random_bun_name

    def random_bun_price(self):
        bun_price = random.randint(100, 9999)
        return bun_price

    def random_bun_price_negative(self):
        bun_price = random.randint(-100, -1)
        return bun_price

    def generate_sause(self):
        data = Data()
        ingredient_name = random.choice(data.ingredients_name_sauces)
        ingredient_price = random.randint(100, 9999)
        ingredient_data = [INGREDIENT_TYPE_SAUCE, ingredient_name, ingredient_price]
        return ingredient_data

    def generate_filling(self):
        data = Data()
        ingredient_name = random.choice(data.ingredients_name_fillings)
        ingredient_price = random.randint(100, 9999)
        ingredient_data = [INGREDIENT_TYPE_FILLING, ingredient_name, ingredient_price]
        return ingredient_data

    def random_ingredient(self):
        ingredient_sauce = self.generate_sause()
        ingredient_filling = self.generate_filling()

        random_ingredient = random.choice([ingredient_sauce, ingredient_filling])
        return random_ingredient


