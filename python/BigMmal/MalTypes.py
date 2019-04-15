class MalType():
    def __init__(self, value):
        self.value = value
class MalSymbol(MalType):
    def __init__(self, value):
        self.value = value

class MalString(MalType):
    def __init__(self, value):
        self.value = value

class MalList(MalType):
    def __init__(self, value):
        self.value = value

class MalVector(MalType):
    def __init__(self, value):
        self.value = value

class MalInt(MalType):
    def __init__(self, _value:int):
        self.value:int = _value
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
EmptyList = MalList([])
class MalBool(MalType):
    def __init__(self, value: bool):
        self.value = value
    def __set__(self, instance, value):
        if(isinstance(value, bool)):
            self.value = value
            return value
        else:
            return Null
    def __bool__(self):
        return self.value
    def __neg__(self):
        self.value = not(self.value)
        return self.value
class MalTrue(MalType):
    def __init__(self):
        self.value = True
    def __bool__(self):
        return True
    def __neg__(self):
        return MalFalse

class MalFalse(MalType):
    def __init__(self):
        self.value = False

    def __bool__(self):
        return False

    def __neg__(self):
        return MalTrue


class Null(MalType):
    def __init__(self):
        self.value = None

class MalFunction(MalType):
    def __init__(self, EVAL, Env, ast, env, parameters):
        self.EVAL = EVAL #The eval function being passsed along
        self.Env = Env #The enviornment class
        self.ast = ast #Tree to work on
        self.env = env #the instance of Env to work on
        self.parameters = parameters #parameters to the funtion
    def fn(self, args):
        return self.EVAL(self.ast, self.Env(self.env, self.parameters, MalList(args)))
    def __call__(self, *args):
        return self.fn(args)
