from mocks.mocks_database import DatabaseMocks


class TestDatabase:
    def test_available_buns_mock_buns(self, database):
        expected_buns = DatabaseMocks.mock_expected_buns()
        # Подменяем список булок в базе данных на моки
        database.buns = expected_buns
        # Проверяем, что возвращается список моков Bun
        actual_buns = database.available_buns()

        # Проверяем, что результат соответствует ожиданиям
        assert actual_buns == expected_buns

    def test_available_ingredients_mock_ingredients(self, database):
        expected_ingredients = DatabaseMocks.mock_expected_ingredients()
        # Подменяем список ингридиентов в базе данных на моки
        database.ingredients = expected_ingredients
        # Проверяем, что возвращается список моков Ingridients
        actual_ingridients = database.available_ingredients()

        # Проверяем, что результат соответствует ожиданиям
        assert actual_ingridients == expected_ingredients
