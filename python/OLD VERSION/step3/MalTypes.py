import sys
class MalType():
    def __init__(self, value):
        self.value = value
class MalList(MalType):
    def __init__(self, value:list = []):
        self.value = value
    def add(self, thing):
        self.value.append(thing)

    def __getitem__(self, item):
        try:
            return self.value[item]
        except:
            raise Exception(item)
            sys.exit(1)
    def __len__(self):
        return len(self.value)
    def toString(self):
        o = ""
        for i in self.value:
            o += ','.join(i.toString())
            o += " "
        o = o[:-1]
        return '(' + o + ')'
    def list(self):
        return self.value
    #def value(self):
    #    return self.value

class MalVector(MalType):
    def __init__(self, value: list = []):
        self.value = value

    def add(self, thing):
        self.value.append(thing)

    def len(self):
        return self.value.len()

    def toString(self):
        o = ""
        for i in self.value:
            o += ','.join(i.toString())
            o += " "
        o = o[:-1]
        return '(' + o + ')'
    def __getitem__(self, item):
        try:
            return self.value[item]
        except:
            raise Exception(item)
            sys.exit(1)

    def list(self):
        return self.value

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
    def __len__(self):
        return 1
class MalFunction(MalType):
    def __init__(self, EVAL, Env, env, tree, parameters:MalSymbol):
        self.EVAL = EVAL
        self.Env = Env
        self.env = env
        self.tree = tree
        self.parameters = parameters
        print("MEME "  + str(type(parameters)))
    def fn(self, *args):
        #print("MEMaaaaaaaaaaaaE " + str(type(self.parameters)))
        #print("treee " + str(self.tree))
        #print("park " + str(self.parameters))
        #print("par " +str(self.parameters.value))
        #print("BLARRGS " + str(args))
        #print("MEMaaaaaE " + str(type(self.parameters)))
        return self.EVAL(self.tree, self.Env(self.env, self.parameters, MalList(args)))

    def __call__(self, *args):
        return self.fn(args)

class MalBool(MalType):
    def __init__(self, value: bool):
        self.value = value
    def __set__(self, instance, value):
        self.value = value
        return value
    def __bool__(self):
        return self.value
    def __neg__(self):
        self.value = not(self.value)
        return self.value


class Null(MalType):
    def __init__(self):
        self.value = None
def MalNourished():
    return Null
class MalString(MalType):
    def __init__(self, value:str = ""):
        self.value = value
    def __add__(self, other):
        return self.value + other
SYMBOLS = [""]