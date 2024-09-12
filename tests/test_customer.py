import pytest

from coffee_shop import Coffee, Customer


@pytest.fixture
def customer() -> Customer:
    """Create a new customer fixture for testing."""
    return Customer("Test Customer")


@pytest.fixture
def coffee() -> Coffee:
    """Create a new coffee fixture for testing."""
    return Coffee("Test Coffee")


def test_customer_name(customer):
    assert customer.name == "Test Customer"


def test_customer_orders(customer, coffee):
    customer.place_order(coffee, 10.0)
    assert len(customer.orders()) == 1


def test_customer_get_coffees(customer, coffee):
    customer.place_order(coffee, 10.0)
    assert len(customer.get_coffees()) == 1


def test_customer_most_aficianado(customer, coffee):
    customer.place_order(coffee, 10.0)
    assert customer.most_aficianado(coffee) == "Test Customer"
