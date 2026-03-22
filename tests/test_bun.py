import pytest

from praktikum.bun import Bun


class TestBun:

    bun = Bun("red bun", 300)

    @pytest.mark.parametrize(
        "name, price",
        [
            ("black bun", 100),
            ("white bun", 200.5),
        ]
    )
    def test_bun_init_sets_attributes(self, name, price):
        bun = Bun(name, price)

        assert bun.name == name
        assert bun.price == price

    def test_get_name_returns_name(self):
        assert self.bun.get_name() == "red bun"

    def test_get_price_returns_price(self):
        assert self.bun.get_price() == 300