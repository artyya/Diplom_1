import pytest

from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestDatabase:

    database = Database()

    @pytest.mark.parametrize(
        "index, name, price",
        [
            (0, "black bun", 100),
            (1, "white bun", 200),
            (2, "red bun", 300),
        ]
    )
    def test_database_contains_expected_buns(self, index, name, price):
        bun = self.database.available_buns()[index]

        assert bun.get_name() == name
        assert bun.get_price() == price

    @pytest.mark.parametrize(
        "index, ingredient_type, name, price",
        [
            (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
            (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            (5, INGREDIENT_TYPE_FILLING, "sausage", 300),
        ]
    )
    def test_database_contains_expected_ingredients(self, index, ingredient_type, name, price):
        ingredient = self.database.available_ingredients()[index]

        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

    def test_available_buns_returns_database_buns(self):
        assert self.database.available_buns() == self.database.buns

    def test_available_ingredients_returns_database_ingredients(self):
        assert self.database.available_ingredients() == self.database.ingredients