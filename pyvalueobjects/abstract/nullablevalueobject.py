
def build_nullable(cls):
    class Nullable(cls):

        def __init__(self, value):
            if value is None:
                self._value = None
            else:
                super().__init__(value)

    return Nullable
