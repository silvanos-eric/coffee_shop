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
