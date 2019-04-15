class MalType():
    def __init__(self, value):
        self.value = value
class MalList(MalType):
    def __init__(self, items:list = []):
        self.items = items
    def add(self, thing):
        self.items.append(thing)

    def __getitem__(self, item):
        return self.items[item]
    def len(self):
        return self.items.len()
    def toString(self):
        o = ""
        for i in self.items:
            o += ','.join(i.toString())
            o += " "
        o = o[:-1]
        return '(' + o + ')'
    def list(self):
        return self.items
    def value(self):
        return self.items

class MalVector(MalType):
    def __init__(self, items: list = []):
        self.items = items

    def add(self, thing):
        self.items.append(thing)

    def len(self):
        return self.items.len()

    def toString(self):
        o = ""
        for i in self.items:
            o += ','.join(i.toString())
            o += " "
        o = o[:-1]
        return '(' + o + ')'

    def list(self):
        return self.items

class MalSymbol(MalType):
    def __init__(self, value):
        self.value = value
    def toString(self):
        return self.value
    def __str__(self):
        return self.value
    def string(self):
        return self.value

class MalInt(MalType):
    def __init__(self, _value:int):
        self.value:int = _value
    def toString(self):
        return self.value.__str__()
    def __add__(self, other):
        return other + self.value
    def __sub__(self, other):
        return other - self.value
    def __int__(self):
        return self.value
    def __str__(self):
        return str(self.value)
    def __mul__(self, other):
        return other * self.value
    def __pow__(self, power, modulo=None):
        return self.value**power

SYMBOLS = [""]