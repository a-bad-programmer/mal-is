class MalType():
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "\\\\" + str(type(self)).replace("BigMmal.MalTypes.", "").replace("<class ", "").replace(">", "") + "(" + str(self.value) + ")" + "// "

class MalSymbol(MalType):
    def __init__(self, value):
        self.value = value

class MalString(MalType):
    def __init__(self, value):
        self.value = value
    def replace(self, a, b):
        self.value.replace(a,b)
    def __str__(self):
        return "\\\\" + str(type(self)).replace("BigMmal.MalTypes.", "").replace("<class ", "").replace(">", "") + "(" " \"" + str(self.value) + "\"" + ")" + "// "

class ListLike(MalType):
    def __init__(self):
        super(self)

class MalList(ListLike):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        out = []
        for i in self.value:
            out += str(i)
        return " ⦓ " + "".join(out) + " ⦔ "

class MalVector(ListLike):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        out = []
        for i in self.value:
            out += str(i)
        return " ⟪ " + "".join(out) + " ⟫ "

class MalInt(MalType):
    def __init__(self, _value:int):
        self.value:int = _value
    def __add__(self, other):
        return other + self.value
    def __sub__(self, other):
        return other - self.value
    def __int__(self):
        return self.value
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
    def __eq__(self, other):
        return self.value == other

MalTrue = MalBool(True)
MalFalse = MalBool(False)


class Null(MalType):
    def __init__(self):
        self.value = None
    def __eq__(self, other):
        return self.value == other

class MalFunction(MalType): # Named for what it likes to do
    def fn(self, *args):
        #print(str(args[0][0].value) + " GARLDs ")

        OUT = self.EVAL(self.ast, self.Env(self.env, self.parameters, MalList(list(args))))
        print("OUT " +  str(OUT))
        return OUT

    def __init__(self, EVAL, Env, ast, env, parameters):
        self.EVAL = EVAL #The eval function being passsed along
        self.Env = Env #The enviornment class
        self.ast = ast #Tree to work on
        self.env = env #the instance of Env to work on
        self.parameters = parameters #parameters to the funtion
        self.__ast__ = self.ast
        self.__gen_env__ = lambda args: Env(env, parameters, args)

        self.isMacro = False # Bum Bum, Macros are dumb

        # self.__ast__ = self.ast
        #self.__gen_env__ = self.fn.__gen_env__

    def __call__(self, *args):
        return self.fn(*args)
    def __str__(self):
        return "<ƒuntion>"
class Atom(MalType):
    def __init__(self, value:MalType):
        self.value = value
    def __str__(self):
        return " ATOM({})".format(self.value.__str__())
    def set(self, nv):
        self.value = nv
    def get(self):
        return self.value

def isSeq(a):
    return isinstance(a, MalList) or isinstance(a, MalVector)

class MalException(MalType, Exception):
    def __init__(self, exception):
        self.exception = exception

def keywordify(string : MalString):
    if(isinstance(string, str)):
        string = MalString(string)
    if(string.value[0]) == "\u029e":
        return string
    else:
        return MalString("\u029e" + string.value)

class MalMap(MalType):
    def __init__(self,hey_this_is_just_a_dictionary : dict):
        self.value = hey_this_is_just_a_dictionary

def isMap(a):
    return isinstance(a, MalMap)

def ezhash(listo):
    if(isinstance(listo, MalList)):
        listo = MalList.value
    out = {}
    for x in range(0, len(listo), 2):
        out[listo[x]] = listo[x + 1]
    return MalMap(out)