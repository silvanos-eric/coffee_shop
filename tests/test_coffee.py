import pytest

from coffee_shop import Coffee, Customer, Order


@pytest.fixture
def coffee() -> Coffee:
    """Create a new coffee fixture for testing."""
    return Coffee("Test Coffee")


@pytest.fixture
def customer() -> Customer:
    """Create a new customer fixture for testing."""
    return Customer("Test Customer")


def test_coffee_name(coffee: Coffee) -> None:
    """Test the name property of Coffee."""
    assert coffee.name == "Test Coffee"


def test_coffee_name_setter(coffee: Coffee) -> None:
    """Test the name setter of Coffee."""
    coffee.name = "New Coffee Name"
    assert coffee.name == "New Coffee Name"


def test_coffee_name_setter_error(coffee: Coffee) -> None:
    """Test the name setter of Coffee with an invalid name."""
    with pytest.raises(ValueError):
        coffee.name = "T"


def test_coffee_orders(coffee: Coffee, customer: Customer) -> None:
    """Test the orders method of Coffee."""
    Order(customer, coffee, 10.0)
    assert len(coffee.orders()) == 1


def test_coffee_customers(coffee: Coffee, customer: Customer) -> None:
    """Test the customers method of Coffee."""
    Order(customer, coffee, 10.0)
    assert coffee.customers() == {customer}


def test_coffee_num_orders(coffee: Coffee, customer: Customer) -> None:
    """Test the num_orders method of Coffee."""
    Order(customer, coffee, 10.0)
    assert coffee.num_orders() == 1


def test_coffee_average_price(coffee: Coffee, customer: Customer) -> None:
    """Test the average_price method of Coffee."""
    Order(customer, coffee, 10.0)
    assert coffee.average_price() == 10.0
