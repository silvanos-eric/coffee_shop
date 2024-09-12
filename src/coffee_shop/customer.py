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

    def create_order(self, coffee, price):
        Order(self, coffee, price)

    @staticmethod
    def most_aficianado(coffee):
        coffee_orders = (order for order in Order if order.coffee == coffee)
        if not coffee_orders:
            return 'None'
        else:
            customer_total_spent = {}
            for order in coffee_orders:
                customer_total_spent[
                    order.customer] = customer_total_spent.get(
                        order.customer, 0) + order.price
            return max(customer_total_spent, key=customer_total_spent.get)
