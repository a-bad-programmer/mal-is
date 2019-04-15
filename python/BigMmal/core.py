from BigMmal.MalTypes import *
from BigMmal import printer

ns = {MalSymbol('+'): lambda a,b: int(a)+int(b), MalSymbol('-'): lambda a,b: int(a)-int(b), MalSymbol('/'): lambda a,b:
(int(a)/int(b)), MalSymbol('*'): lambda a,b: int(a)*int(b),MalSymbol('^'): lambda a,b: int(a)**int(b)}
"""repl_env = Env()
repl_env.seto((MalSymbol('+'), lambda a,b: int(a)+int(b))
repl_env.seto(MalSymbol('-'), lambda a,b: int(a)-int(b))
repl_env.seto(MalSymbol('/'), lambda a,b: int(int(a)/int(b)))
repl_env.seto(MalSymbol('*'), lambda a,b: int(a)*int(b))
repl_env.seto(MalSymbol('^'), lambda a,b: int(a)**int(b))"""

def prn(process):
    printer.pr_str(process)
    return Null
def list(*args):
    out = []
    for i in args:
        out.append(i)
    return MalList(out)
def isList(maybe_a_list):
    return isinstance(maybe_a_list, MalList)
def isEmpty(maybe_empty):
    return maybe_empty.value == []
def count(to_be_counted):
    return len(to_be_counted.value)
def equals(a, b):
    if(type(a) == type(b)):
        if(isList(a)):
            if(count(a) == count(b)):
                for i in len(a.value):
                    if(a.value[i] == b.value[i]):
                        continue
                    else:
                        return MalFalse
        elif(a.value == b.value):
            return MalTrue
        return MalFalse

def lessThan(a,b):
    return a.value < b.value
def lessThanEq (a,b):
    return a.value <= b.value
def greaterThan(a,b):
    return a.value > b.value
def greaterThanEq (a,b):
    return a.value >= b.value