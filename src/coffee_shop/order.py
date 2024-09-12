from customer import Customer
from coffee import Coffee


class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        # Add this order to the class-level all_orders list
        Order.all_orders.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError('Customer must be of type Customer!')
        else:
            self._customer = customer

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        if not isinstance(coffee, Coffee):
            raise TypeError('Coffee must of type Coffeee!')
        else:
            self._coffee = coffee

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0!")
