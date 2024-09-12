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
