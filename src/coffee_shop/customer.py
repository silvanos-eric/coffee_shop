from order import Order


class Customer:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not (1 <= len(name) <= 15):
            raise ValueError(
                'Customer name must be between 1 and 15 characters!')
        else:
            self._name = name

    def orders(self):
        return [order for order in Order if order.customer == self]

    def coffees(self):
        return list({
            order.coffee
            for order in Order.all_orders if order.customer == self
        })
