from unittest.mock import Mock

from practikum.ingredient_types import *


class DatabaseMocks:
    @staticmethod
    def mock_expected_buns():
        mock_bun1 = Mock()
        mock_bun1.get_name.return_value = "black bun"
        mock_bun1.get_price.return_value = 100

        mock_bun2 = Mock()
        mock_bun2.get_name.return_value = "white bun"
        mock_bun2.get_price.return_value = 200

        mock_bun3 = Mock()
        mock_bun3.get_name.return_value = "red bun"
        mock_bun3.get_price.return_value = 300

        # Ожидаемый список булочек
        expected_buns = [mock_bun1, mock_bun2, mock_bun3]

        return expected_buns

    @staticmethod
    def mock_expected_ingredients():
        # Создаем моки объектов Ingredient
        mock_sauce1 = Mock()
        mock_sauce1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_sauce1.get_name.return_value = "hot sauce"
        mock_sauce1.get_price.return_value = 100

        mock_sauce2 = Mock()
        mock_sauce2.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_sauce2.get_name.return_value = "sour cream"
        mock_sauce2.get_price.return_value = 200

        mock_sauce3 = Mock()
        mock_sauce3.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_sauce3.get_name.return_value = "chili sauce"
        mock_sauce3.get_price.return_value = 300

        mock_filling1 = Mock()
        mock_filling1.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_filling1.get_name.return_value = "cutlet"
        mock_filling1.get_price.return_value = 100

        mock_filling2 = Mock()
        mock_filling2.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_filling2.get_name.return_value = "dinosaur"
        mock_filling2.get_price.return_value = 200

        mock_filling3 = Mock()
        mock_filling3.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_filling3.get_name.return_value = "sausage"
        mock_filling3.get_price.return_value = 300

        # Ожидаемый список ингредиентов
        expected_ingredients = [mock_sauce1, mock_sauce2, mock_sauce3,
                                mock_filling1, mock_filling2, mock_filling3]

        return expected_ingredients