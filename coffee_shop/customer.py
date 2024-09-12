from . import Coffee, Customer, Order


class Customer:

    def __init__(self, name: str):
        """ Create a new Customer object. """
        self._name = name

    @property
    def name(self) -> str:
        """Customer name."""
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """Set customer name."""
        if not 1 <= len(name) <= 15:
            raise ValueError(
                "Customer name must be between 1 and 15 characters!")
        self._name = name

    def orders(self):
        """Get all orders associated with this customer."""
        return [order for order in Order.all_orders if order.customer == self]

    def get_coffees(self):
        """
        Get a list of distinct coffees this customer has ordered.
        """
        return list({
            order.coffee
            for order in Order.all_orders if order.customer == self
        })

    def place_order(self, coffee: Coffee, price: float) -> None:
        """Create a new order for this customer for the given coffee."""
        Order(self, coffee, price)

    @staticmethod
    def most_aficianado(coffee: Coffee) -> str:
        """
        The customer who has spent the most money on the given coffee.
        """
        # Get all orders associated with this coffee
        coffee_orders = [
            order for order in Order.all_orders if order.coffee == coffee
        ]

        if not coffee_orders:
            return 'None'

        # Map customers to total amount spent on this coffee
        customer_spending = {}
        for order in coffee_orders:
            customer_spending[order.customer] = customer_spending.get(
                order.customer, 0) + order.price

        # Return the customer who has spent the most
        return max(customer_spending, key=customer_spending.get)
