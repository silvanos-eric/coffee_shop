from order import Order


class Coffee:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not (len(name) < 3):
            raise ValueError('Coffee name must be at least 3 characters long!')
        else:
            self._name = name

    def orders(self):
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self):
        return list({
            order.customer
            for order in Order.all_orders if order.coffee == self
        })

    def num_orders(self):
        return len(order for order in Order if order.coffee == self)

    def average_price(self):
        return sum(order.price for order in Order
                   if order.coffee == self) / self.num_orders()
