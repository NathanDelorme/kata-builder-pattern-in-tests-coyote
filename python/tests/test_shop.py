from shop import Shop, Address
from tests.user_builder import UserBuilder

def test_happy_path():
    user = UserBuilder().build()

    assert Shop.can_order(user)
    assert not Shop.must_pay_foreign_fee(user)


def test_minors_cannot_order_from_the_shop():
    user = UserBuilder().minor().build()

    assert not Shop.can_order(user)


def test_cannot_order_if_not_verified():
    user = UserBuilder().not_verified().build()

    assert not Shop.can_order(user) # No need to modify the test, this assertion is correct

def test_foreigners_must_be_foreign_fee():
    user = UserBuilder().foreign().build()

    assert Shop.must_pay_foreign_fee(user)
