import sys, re
from step3 import MalTypes
from step3.MalTypes import MalSymbol,MalList,MalType,MalVector,MalInt, MalFunction
from step3 import reader, printer

#repl_env = {'+': lambda a,b: int(a)+int(b), '-': lambda a,b: int(a)-int(b), '/': lambda a,b: int(int(a)/int(b)), '*': lambda a,b: int(a)*int(b), '^': lambda a,b: int(a)**int(b)}
from step3.Env import Env

repl_env = Env()
repl_env.seto(MalSymbol('+'), lambda a,b: int(a)+int(b))
repl_env.seto(MalSymbol('-'), lambda a,b: int(a)-int(b))
repl_env.seto(MalSymbol('/'), lambda a,b: int(int(a)/int(b)))
repl_env.seto(MalSymbol('*'), lambda a,b: int(a)*int(b))
repl_env.seto(MalSymbol('^'), lambda a,b: int(a)**int(b))

define = MalSymbol("!def")

def READ(x):
    return(reader.read_str(x))

def EVAL(x, env):
    #print("MEX" + str(type(x)))
    print(str(x.value))
    if not(isinstance(x, MalTypes.MalList) or isinstance(x, MalVector)):
        return eval_ast(x, env)
    print("Presto")
    a0 = x[0]
    try:
        a1 = x[1]
    except:
        a1 = MalTypes.Null
    try:
        a2 = x[2]
    except:
        a2 = MalTypes.Null
    print(str(a0 )+ " 1")
    print(str(a1) + " 2 " + str(type(a1)))
    print(str(a2) + " 3 " + str(type(a2)))
    #print(a0.value + "ADIWDIAWMD")
    if(a0.value == 'def!'):
        #print(a1)
        if (isinstance(a1, str)):
            raise Exception("Kaiba")
        a = env.seto(a1, EVAL(a2, env))
        #print(str(a) + "AAAAHH")
        return a
    elif(a0.value == 'let*'):
        nenv = Env(env)
        if(isinstance(a1, MalList)):
            for i in range(0, int(len(a1)), 2):
                if(isinstance(a1[i], str)):
                    raise Exception("Kaiba")
                nenv.seto(a1[i], EVAL(a1[i + 1], nenv))
        return EVAL(a2, nenv)
    elif(a0.value == 'do'):
        return eval_ast(x[1:],env)[-1]
    elif (a0.value == 'if'):
        one = EVAL(a1, env)
        if(one != False and one != None):
            return EVAL(a2, env)
        if(one == False and len(one) < 3):
            print("HONK HONK !@$!@#(@&$#*^@")
            return None
        else:
            return EVAL(x[3], env)
    elif (a0.value == "fn*"):
        print("Arrrg")
        #print("MUDNDW " + str(type(a2)))
        return MalFunction(EVAL, Env, env, a1, a2)
    else:
        print("MURDER" + str(x))
        evaled = eval_ast(x, env)
        print("evaled " + str(evaled))
        print("evld " + str(evaled.list()))
        return evaled[0](*evaled[1:])


def eval_ast(x:MalTypes.MalType, env):
    print("OOGGOE OMNWF " + str(x))
    if(isinstance(x, MalTypes.MalSymbol)):
        try:
            return env.get(x)
        except:
            raise Exception("Function not found, this is not very functional")
    elif(isinstance(x, MalTypes.MalList)):
        out = []
        for item in x.value:
            out.append(EVAL(item, env))
        return MalTypes.MalList(out)
    elif(isinstance(x, MalTypes.MalVector)):
        out = []
        for item in x.value:
            out.append(EVAL(item, env))
        return MalTypes.MalVector(out)
    else:
        #print("EVL_AST" + str(x))
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
