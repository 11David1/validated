class Validated:

    def __init__(self, **kwargs):

        for element in kwargs.items():
            setattr(self, self.name, self.value)

    def __str__(self):
        pass


class Field:
    def __set__(self, obj, value):
        if self.validate(value):
            setattr(obj, self.internale_name, value)

    def __get__(self, obj, instance):
        return getattr(obj, self.internale_name)

    def __set_name__(self, owner, name):
        self.name = name
        self.internale_name = "_" + name


# Integer.__init__ läuft genau einmal, und zwar
# wenn die Klasse Person definiert wird
class Integer(Field):
    def __init__(self, min_value=None, max_value=None):
        super().__init__()
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, value):
        if isinstance(value, int) and self.min_value <= value <= self.max_value:
            return True
        raise ValueError(
            f"{self.name} muss zwischen {self.min_value} und {self.max_value} sein"
        )


class String(Field):
    def __init__(self, min_len=None, max_len=None):
        super().__init__()
        self.min_len = min_len
        self.max_len = max_len

    def validate(self, value):
        if isinstance(value, str) and self.min_len <= len(value) <= self.max_len:
            return True
        raise ValueError(
            f"{self.name} muss zwischen {self.min_len} und {self.max_len} Zeichen lang sein."
        )


class Float(Field):
    def __init__(self, min_value=None):
        super().__init__()
        self.min_value = min_value

    def validate(self, value):
        if isinstance(value, (float, int)) and self.min_value <= value:
            return True  # bool kommt noch durch
        raise ValueError(f"{self.name} muss größer / gleich {self.min_value} sein.")
