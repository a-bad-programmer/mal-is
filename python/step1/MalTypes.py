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
        return o
    def list(self):
        return self.items

class Symbol():
    def __init__(self, _string):
        self.string = _string
    def type(self):
        return
    def toString(self):
        return self.string
    def __str__(self):
        return self.string
SYMBOLS = [""]