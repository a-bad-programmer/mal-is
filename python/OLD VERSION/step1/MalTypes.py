class MalList():
    def __init__(self, items:list = []):
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

class MalVector():
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

class Symbol():
    def __init__(self, _string):
        self.string = _string
    def toString(self):
        return self.string
    def __str__(self):
        return self.string

class MalInt():
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

SYMBOLS = [""]