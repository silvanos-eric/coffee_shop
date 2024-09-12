from order import Order
from customer import Customer


class Coffee:

    def __init__(self, name: str):
        """Create a new Coffee object."""
        self._name = name

    @property
    def name(self) -> str:
        """Get the name of this coffee."""
        return self._name

    @name.setter
    def name(self, name_: str) -> None:
        """Set the name of this coffee."""
        if len(name_) < 3:
            raise ValueError("Coffee name must be at least 3 characters long!")
        self._name = name_

    def orders(self) -> list[Order]:
        """Get all orders associated with this coffee."""
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self) -> set[Customer]:
        """Get the set of customers who have ordered this coffee."""
        return {
            order.customer
            for order in Order.all_orders if order.coffee == self
        }

    def num_orders(self) -> int:
        """Get the number of orders associated with this coffee."""
        return len(
            [order for order in Order.all_orders if order.coffee == self])

    def average_price(self) -> float:
        """Get the average price paid for this coffee."""
        total_paid = sum(order.price for order in self.orders())
        return total_paid / self.num_orders()
