import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestIngredient:

    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)

    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (INGREDIENT_TYPE_FILLING, "cutlet", 300),
        ]
    )
    def test_ingredient_init_sets_attributes(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price

    def test_get_price_returns_price(self):
        assert self.ingredient.get_price() == 100

    def test_get_name_returns_name(self):
        assert self.ingredient.get_name() == "hot sauce"

    def test_get_type_returns_type(self):
        assert self.ingredient.get_type() == INGREDIENT_TYPE_SAUCE