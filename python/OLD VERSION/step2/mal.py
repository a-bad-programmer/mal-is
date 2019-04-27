import sys, re
from step2 import MalTypes
from step2 import reader, printer

repl_env = {'+': lambda a,b: int(a)+int(b), '-': lambda a,b: int(a)-int(b), '/': lambda a,b: int(int(a)/int(b)), '*': lambda a,b: int(a)*int(b), '^': lambda a,b: int(a)**int(b)}
def READ(x):
    return(reader.read_str(x))

def EVAL(x, env):
    if(isinstance(x, MalTypes.MalList)):
        if(x.items == []):
            return x
        else:
            evaled = eval_ast(x, env)
            return evaled[0](*evaled[1:])
    else:
        return eval_ast(x, env)
def eval_ast(x:MalTypes.MalType, env):
    if(isinstance(x, MalTypes.MalSymbol)):
        try:
            return env[x.value]
        except:
            raise Exception("Function not found, this is not very functional")
    elif(isinstance(x, MalTypes.MalList)):
        out = []
        for item in x.items:
            out.append(EVAL(item, env))
        return MalTypes.MalList(out)
    else:
        print(x)
        return x
def PRINT(x):
    return printer.pr_str(x)

def rep(x):
    return PRINT(EVAL(READ(x), repl_env))

def repl():
    try:
        x = input()
        print(rep(x))
    except EOFError:
        exit()

while True:
    repl()
