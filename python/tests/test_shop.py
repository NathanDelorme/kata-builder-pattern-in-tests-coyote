from shop import Shop, Address
from tests.user_builder import UserBuilder

builder = UserBuilder()

def test_happy_path():
    user = builder.build()

    assert Shop.can_order(user)
    assert not Shop.must_pay_foreign_fee(user)


def test_minors_cannot_order_from_the_shop():
    builder.set_age(15)
    user = builder.build()

    assert not Shop.can_order(user)


def test_cannot_order_if_not_verified():
    builder.set_verified(False)
    user = builder.build()

    assert not Shop.can_order(user) # No need to modify the test, this assertion is correct

def test_foreigners_must_be_foreign_fee():
    builder.set_address(Address("33 quai d'Orsay", "", "Paris", "75007", "France"))
    user = builder.build()

    assert Shop.must_pay_foreign_fee(user)
