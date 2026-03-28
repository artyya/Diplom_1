import pytest
from unittest.mock import MagicMock

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


class TestBurger:

    def test_set_buns_sets_bun(self):
        burger = Burger()
        bun = MagicMock(spec=Bun)

        burger.set_buns(bun)

        assert burger.bun is bun

    def test_add_ingredient_adds_ingredient_to_list(self):
        burger = Burger()
        ingredient = MagicMock(spec=Ingredient)

        burger.add_ingredient(ingredient)

        assert burger.ingredients == [ingredient]

    def test_remove_ingredient_removes_ingredient_by_index(self):
        burger = Burger()
        first_ingredient = MagicMock(spec=Ingredient)
        second_ingredient = MagicMock(spec=Ingredient)

        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)
        burger.remove_ingredient(0)

        assert burger.ingredients == [second_ingredient]

    def test_move_ingredient_moves_ingredient_to_new_index(self):
        burger = Burger()
        first_ingredient = MagicMock(spec=Ingredient)
        second_ingredient = MagicMock(spec=Ingredient)
        third_ingredient = MagicMock(spec=Ingredient)

        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)
        burger.add_ingredient(third_ingredient)
        burger.move_ingredient(0, 2)

        assert burger.ingredients == [second_ingredient, third_ingredient, first_ingredient]

    @pytest.mark.parametrize(
        'ingredient_prices, expected_price',
        [
            ([], 200),
            ([50], 250),
            ([50, 25], 275),
        ]
    )
    def test_get_price_returns_expected_price(self, ingredient_prices, expected_price):
        burger = Burger()
        bun = MagicMock(spec=Bun)
        bun.get_price.return_value = 100

        burger.set_buns(bun)

        ingredients = []
        for ingredient_price in ingredient_prices:
            ingredient = MagicMock(spec=Ingredient)
            ingredient.get_price.return_value = ingredient_price
            ingredients.append(ingredient)
            burger.add_ingredient(ingredient)

        actual_price = burger.get_price()

        assert actual_price == expected_price
        bun.get_price.assert_called_once()
        for ingredient in ingredients:
            ingredient.get_price.assert_called_once()

    def test_get_receipt_returns_expected_receipt(self):
        burger = Burger()

        bun = MagicMock(spec=Bun)
        bun.get_name.return_value = 'black bun'
        bun.get_price.return_value = 100

        sauce = MagicMock(spec=Ingredient)
        sauce.get_type.return_value = 'SAUCE'
        sauce.get_name.return_value = 'hot sauce'
        sauce.get_price.return_value = 50

        filling = MagicMock(spec=Ingredient)
        filling.get_type.return_value = 'FILLING'
        filling.get_name.return_value = 'cutlet'
        filling.get_price.return_value = 100

        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        actual_receipt = burger.get_receipt()

        expected_receipt = (
            '(==== black bun ====)\n'
            '= sauce hot sauce =\n'
            '= filling cutlet =\n'
            '(==== black bun ====)\n\n'
            'Price: 350'
        )

        assert actual_receipt == expected_receipt