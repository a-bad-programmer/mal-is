from BigMmal import reader, printer, core
from BigMmal.Env import Env
from BigMmal.MalTypes import *

repl_env = Env()

for key in core.ns:
    repl_env.seto(MalSymbol(key), core.ns[key])

def eval_ast(ast, env):
    if isinstance(ast, MalSymbol):
        return env.get(ast)
    elif isinstance(ast, MalList):
        out = []
        for i in ast.value:
            out.append(EVAL(i, env))
        return MalList(out)
    elif isinstance(ast, MalVector):
        out = []
        for i in ast.value:
            out.append(EVAL(i, env))
        return MalVector(out)
    else:
        return ast

def READ(process):
    return reader.read_str(process)
def EVAL(ast, env):
    if not (isinstance(ast, MalList) or isinstance(ast, MalVector)):
        return eval_ast(ast, env)
    elif ast == EmptyList:
        return ast
    else:
        print(ast.value)
        a0 = ast.value[0]
        try:
            a1 = ast.value[1]
            print(str(a0.value) + "AAAAGG1")
        except:
            a1 = Null
        try:
            a2 = ast.value[2]
        except:
            a2 = Null
        if(a0.value == "def!"):
            return env.seto(a1, EVAL(a2, env))
        elif(a0.value == "let*"):
            nenv = Env(env)
            if (isinstance(a1, MalList)):
                for i in range(0, int(len(a1.value)), 2):
                    if (isinstance(a1.value[i], str)):
                        raise Exception("Kaiba")
                    nenv.seto(a1.value[i], EVAL(a1.value[i + 1], nenv))
            return EVAL(a2, nenv)
        elif(a0.value == "do"):
            return eval_ast(ast[1:], env)[-1]
        elif (a0.value == "if"):
            one = EVAL(a1, env)
            if (one != MalFalse and one != Null and one != False and one != None):
                return EVAL(a2, env)
            if (one == False and len(one) < 3):
                print("HONK HONK !@$!@#(@&$#*^@")
                return Null
            else:
                return EVAL(ast[3], env)
        elif (a0.value == "fn*"):
            return MalFunction(EVAL,Env, a2,env,a1 )
        else:
            process = eval_ast(ast, env)
            return process.value[0](*process.value[1:])
def PRINT(process):
    return printer.pr_str(process)
def repl(process):
    return PRINT(EVAL(READ(process), repl_env))

repl("(def! not (fn* (a) (if a false true)))")


while True:
    process = input()
    print(str(repl(process)) + " OUT")