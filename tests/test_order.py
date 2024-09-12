import pytest

from coffee_shop import Order


@pytest.fixture
def order(customer, coffee):
    return Order(customer, coffee, 10.0)


def test_order_customer(order, customer):
    assert order.customer == customer


def test_order_coffee(order, coffee):
    assert order.coffee == coffee


def test_order_price(order):
    assert order.price == 10.0
