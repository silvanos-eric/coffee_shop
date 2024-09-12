from . import Coffee, Customer, Order


class Order:
    all_orders = []

    def __init__(self, customer: Customer, coffee: Coffee, price: float):
        """ Create a new Order object. """
        self.customer = customer
        self.coffee = coffee
        self.price = price
        self.__class__.all_orders.append(self)

    @property
    def customer(self) -> Customer:
        """The customer making the order."""
        return self._customer

    @customer.setter
    def customer(self, customer: Customer) -> None:
        """
        Set the customer for this order.

        Parameters
        ----------
        customer : Customer
            The customer making the order.
        """
        if not isinstance(customer, Customer):
            raise TypeError('Customer must be of type Customer!')
        self._customer = customer

    @property
    def coffee(self) -> Coffee:
        """The coffee being ordered."""
        return self._coffee

    @coffee.setter
    def coffee(self, coffee_: Coffee) -> None:
        """Set the coffee for this order."""
        if not isinstance(coffee_, Coffee):
            raise TypeError("coffee_ must be of type Coffee")
        self._coffee = coffee_

    @property
    def price(self) -> float:
        """The price paid for the coffee."""
        return self._price

    @price.setter
    def price(self, price: float) -> None:
        """ Set the price for this order. """
        if not 1.0 <= price <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0!")
