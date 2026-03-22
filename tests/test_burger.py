from unittest.mock import MagicMock

from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestBurger:

    def test_burger_init_sets_default_values(self):
        burger = Burger()

        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns_sets_bun(self):
        burger = Burger()
        bun = MagicMock()

        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient_adds_ingredient_to_list(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)

        burger.add_ingredient(ingredient)

        assert burger.ingredients == [ingredient]

    def test_remove_ingredient_removes_ingredient_by_index(self):
        burger = Burger()
        first_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        second_ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200)

        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)

        burger.remove_ingredient(0)

        assert burger.ingredients == [second_ingredient]

    def test_move_ingredient_moves_ingredient_to_new_index(self):
        burger = Burger()
        first_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        second_ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200)
        third_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300)

        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)
        burger.add_ingredient(third_ingredient)

        burger.move_ingredient(0, 2)

        assert burger.ingredients == [second_ingredient, third_ingredient, first_ingredient]

    def test_get_price_returns_sum_of_bun_and_ingredients_prices(self):
        burger = Burger()

        bun = MagicMock()
        bun.get_price.return_value = 100

        first_ingredient = MagicMock()
        first_ingredient.get_price.return_value = 50

        second_ingredient = MagicMock()
        second_ingredient.get_price.return_value = 25

        burger.set_buns(bun)
        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)

        price = burger.get_price()

        assert price == 275
        bun.get_price.assert_called_once()
        first_ingredient.get_price.assert_called_once()
        second_ingredient.get_price.assert_called_once()

    def test_get_receipt_returns_expected_string(self):
        burger = Burger()

        bun = MagicMock()
        bun.get_name.return_value = "black bun"
        bun.get_price.return_value = 100

        sauce = MagicMock()
        sauce.get_type.return_value = "SAUCE"
        sauce.get_name.return_value = "hot sauce"
        sauce.get_price.return_value = 50

        filling = MagicMock()
        filling.get_type.return_value = "FILLING"
        filling.get_name.return_value = "cutlet"
        filling.get_price.return_value = 100

        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        receipt = burger.get_receipt()

        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "= filling cutlet =\n"
            "(==== black bun ====)\n\n"
            "Price: 350"
        )

        assert receipt == expected_receipt