from BigMmal.MalTypes import *
from BigMmal import printer, reader
import warnings

ns = {MalSymbol('+'): lambda a,b: MalInt(int(a)+int(b)),
      MalSymbol('-'): lambda a,b: MalInt(int(a)-int(b)),
      MalSymbol('/'): lambda a,b: MalInt(int(int(a)/int(b))),
      MalSymbol('*'): lambda a,b: MalInt(int(a)*int(b)),
      MalSymbol('^'): lambda a,b: MalInt(int(a)**int(b)),
      MalSymbol("read-string"): lambda a:read_string(a),
      MalSymbol("pr-str"): lambda *args: print_str(*args),
      MalSymbol("str"): lambda *args: string(*args),
      MalSymbol("println"): lambda *args: println(*args),
      MalSymbol("slurp"): lambda a: slurp(a),
      MalSymbol("swap!"): lambda a, b, *args: swap_(a, b, *args),
      MalSymbol("atom"): lambda a: _atom(a),
      MalSymbol("deref"): lambda a: deref(a),
      MalSymbol("reset!"): lambda a, b: reset_(a,b),
      MalSymbol("atom?"): lambda a: isAtom(a),
      MalSymbol("="): lambda a,b: equals_(a,b),
      MalSymbol("nil"): Null,
      MalSymbol("prn"): lambda a: prn(a),
      MalSymbol("cons"): lambda a,b: cons(a,b),
      MalSymbol("concat"): lambda *args: concat(*args),
      MalSymbol("nth"): lambda a,b: nth(a,b),
      MalSymbol("first"): lambda a: first(a),
      MalSymbol("rest"): lambda  a: rest(a),
      MalSymbol("empty?"): lambda a: isEmpty(a),
      MalSymbol("count"): lambda a: count(a),
      MalSymbol("<"): lambda a,b: lessThan(a,b),
      MalSymbol(">"): lambda a,b: greaterThan(a,b),
      MalSymbol("<="): lambda a,b: lessThanEq(a,b),
      MalSymbol(">="): lambda a,b: greaterThanEq(a,b),
      MalSymbol("throw"): lambda a: throw(a),
      MalSymbol("hash-map"): lambda args: ezhash(list(*args)),
      MalSymbol("map?"): lambda a: isMap(a),
      MalSymbol("assoc"): lambda a, *args: assoc(a, *args),
      MalSymbol("deassoc"): lambda a, *args: deassoc(a, *args),
      MalSymbol("get"): lambda hasho, key: get_(hasho, key),
      MalSymbol("contains?"): lambda hasho, key: contains(hasho, key),
      MalSymbol("keys"): lambda hasho: keys(hasho),
      MalSymbol("vals"): lambda  hasho: vals(hasho),
      MalSymbol("sequential?"): lambda a: isSeq(a),
      MalSymbol("keyword"): lambda  a: keywordify(a),
      MalSymbol("?keyword"): lambda a: isKeyword(a),
      MalSymbol("symbol"): lambda a: makeSymbol(a),
      MalSymbol("list"): lambda a: makeList(a),
      MalSymbol("list?"): lambda a: isList(a)}


"""repl_env = Env()
repl_env.seto((MalSymbol('+'), lambda a,b: int(a)+int(b))
repl_env.seto(MalSymbol('-'), lambda a,b: int(a)-int(b))
repl_env.seto(MalSymbol('/'), lambda a,b: int(int(a)/int(b))) # Old version of doing namespace
repl_env.seto(MalSymbol('*'), lambda a,b: int(a)*int(b))
repl_env.seto(MalSymbol('^'), lambda a,b: int(a)**int(b))"""


def prn(*args):
    out = []
    for i in args:
        out.append(print_str(MalList(i)))
    print(" ".join(out))
    return Null
def List(*argv):
    out = []
    print(str(argv) + "Scloop")
    for i in argv[0]:
        print(str(i) + " POOP")
        if(isinstance(i, MalList)):
            print("BUHDJAW")
            i = List(i)
        out.append(i)
    return MalList(out)
def isList(maybe_a_list):
    return MalBool(isinstance(maybe_a_list, MalList)).value
def isEmpty(maybe_empty):
    if(isinstance(maybe_empty, ListLike)):
        return MalBool(not len(maybe_empty.value) > 0)
    else:
        return MalBool(not len(maybe_empty) > 0)
def count(to_be_counted):
    if(isinstance(to_be_counted, ListLike)):
        return MalInt(len(to_be_counted.value))
    elif(isNull(to_be_counted)):
        return MalInt(0)
    else:
        return MalInt(len(to_be_counted))
'''def equals(a, b):
    if(type(a) == type(b)):
        if(isList(a)):
            if(count(a) == count(b)):
                for i in len(a.value):
                    if(a.value[i] == b.value[i]):
                        continue
                    else:
                        return MalFalse # Forgot I made these, wrote a new one that works. This is untested
        elif(a.value == b.value):
            return MalTrue
        return MalFalse'''

def lessThan(a,b):
    return MalBool(a.value < b.value)
def lessThanEq (a,b):
    return MalBool(a.value <= b.value)
def greaterThan(a,b):
    return MalBool(a.value > b.value)
def greaterThanEq (a,b):
    return MalBool(a.value >= b.value)

def read_string(process):
    if(isinstance(process, MalString)):
        out = reader.read_str(process.value)
        return out
    else:

        out = reader.read_str(process)
        return out

def slurp(fileName):

    if(isinstance(fileName, MalString)):
        path = fileName.value
    else:
        path = fileName
    if (isinstance(path, tuple)):
        path = path[0]
    f = open(path, "r")
    ooout = []
    for line in f:
        if(line[-1]) == "\n":
            proc = line[:-1]
        else:
            proc = line
        ooout.append(proc)
    ooout.reverse() # Do this because the mal will process outward in a long chain of things
    out = " ".join(ooout)
    f.close()
    return MalString(out)

def print_str(*args):
    out = []
    for i in args:
        if(isinstance(i, bool)):
            i = MalBool(i)
        out.append(printer.pr_str(i.value))
    return " ".join(out)

def string(*args):
    out = []
    for i in args:
        out.append(printer.pr_str(i, False))
    return "".join(out)

    print(str(out) + " ZZZ Z")
    return MalString(out)

def println(*args):
    out = []
    for i in args:
        out.append(printer.pr_str(i, MalBool(False)))
    return " ".join(out)

def _atom(value):
    if not ((isinstance(value, MalType))):
        raise Exception ("Maybe ignore this but a non-mal type is in an atom, {} found ".format(type(value)))
    return Atom(value)
def isAtom(value):
    return MalBool(isinstance(value, Atom))

def deref(value):
    if not (isAtom(value)):
        warnings.warn("Hey, another warning here but you are deref-ing a non Atom")
    return value.value
def reset_(atom_ : Atom, value):
    atom_.set(value)
    return value
def swap_(atom_ : Atom, func, *args):
    atom_.value = func(atom_.get(), *args)
    wumwum = atom_.value
    return atom_.get()

def equals_(a, b):
    if(isinstance(a, MalType) and isinstance(b, MalType)):
        if(isSeq(a)):
            if(isSeq(b)):
                if(len(a.value) != len(b.value)):
                    return False
                for i in range(len(a.value)):
                    if(equals_(a.value[i], b.value[i])):
                        continue
                    else:
                        return False
                return True
            else:
                return False
        else:
            return (a.value == b.value and type(a) == type(b))
    else:
        return (a == b)

def cons(add, listo : MalList):
    out = []
    out = out + listo.value
    out.insert(0, add)
    return MalList(out)

def concat(*args):
    out = []
    for i in args:
        if not isinstance(i, MalList):
            raise Exception("Concatinating non-list type: {}".format(type(i)))
        out = out + i.value
    return MalList(out)

def nth(list, pos):
    if(isinstance(pos, MalInt)):
        pos = pos.value
    return list.value[pos]
def first(listo):
    if(isinstance(listo, tuple)):
        if len(listo) == 0:
            listo = EmptyList
    if(isinstance(listo, list)):
        listo = MalList(listo)
    if(listo.value == []):
        return Null
    if(listo == Null or listo is None):
        return Null
    return listo.value[0]
def rest(listo):
    if(isinstance(listo, tuple)):
        if len(listo) == 0:
            listo = EmptyList
    if(isinstance(listo, list)):
        listo = MalList(listo)
    return MalList(listo.value[1:])

def throw(a):
    print(str(a) + " THis is a bad " + str(a.value))
    if(isinstance(a, MalType)):
        raise MalException(a.value)
    else:
        raise MalException(a)

def apply(a, *args):
    last = args[-1]
    tmpout = []
    for i in args[:-1]:
        tmpout += i
    if(isList(last)):
        out = concat(tmpout, last)
        return out
    else:
        raise Exception("woops, last element of an apply is non-list: {}".format(type(last)))

def map(func, listo):
    out = []
    for i in listo.value:
        out.append(func(i))
    return out
def isNull(a):
    b = type (a)
    return isinstance(a, Null) or a is None

def isTrue(a):
    return a == MalTrue
def isFalse(a):
    return a == MalFalse

def isSymbol(a):
    return isinstance(a, MalSymbol)
'''def isEmpty(list):
    if(not isList(list)):
        raise Exception("isEmpty run on non-list type: {}".format(type(list)))
    if(list.value == []):
        return True # Duplicate, forgot I made this before but never added to ns
    return False'''

def assoc(a, *args):
    if(not isMap(a)):
        raise Exception("assoc-ing non-hashmap thing: {}" + str(type(a)))
    press = list(args)
    #out = dict(a.value, **ezhash(list(args)).value)
    out = {}
    out.update(a.value)
    out.update(ezhash(list(args)).value)
    return MalMap(out)

def deassoc(a, *args):
    out = {}
    for key in a.value.keys:
        if key in args:
            pass
        else:
            out[key] = a.value[key]
    return MalMap(out)

def get_(hasho, key):
    if(key in hasho.value):
        return hasho.value[key]
    else:
        return Null

def contains(hasho, key):
    for i in hasho.value:
        if(equals_(i, key)):
            return MalTrue
        else:
            return MalFalse

def keys(hasho):
    return MalList(hasho.value.keys())
def vals(hasho):
    return MalList(hasho.value.values())
def isKeyword(a):
    return (isinstance(a, MalString)) and a.value[0] == "\u029e"

def isString(a):
    return (isinstance(a, MalString)) and not a.value[0] == "\u029e"

def makeSymbol(a):
    if(isinstance(a, MalString)):
        return MalSymbol(a.value)
    elif not isinstance(a, MalType):
        if(isinstance(a, str)):
            return MalSymbol(a)
    raise Exception("BAD SYMBOL " + str(type(a)) + " is not a symbol!")

def makeList(*args):
    return MalList(list(*args))

def isList(a):
    return isinstance(a, MalList)