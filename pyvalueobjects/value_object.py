
class ValueObject:

    def __init__(self, value):
        self._value = value

    def value(self):
        return self._value

    def str_value(self) -> str:
        return str(self._value)
