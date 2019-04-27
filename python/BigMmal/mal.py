from BigMmal import reader, printer, core
from BigMmal.Env import Env
from BigMmal.MalTypes import *
from BigMmal.core import *
#import pdb; pdb.set_trace()
repl_env = Env()

for key in core.ns:
    repl_env.seto(key, core.ns[key])
    print("set " + str(key.value) + " to " + str(core.ns[key]))
repl_env.seto(MalSymbol("eval"), lambda ast: EVAL(ast, repl_env))

def eval_ast(ast, env):
    #print(str(" LOOKIE" + "OOOPeval " + str(ast.value) + "    " + str(ast)))
    if isinstance(ast, MalSymbol):
        return env.get(ast)
    elif isinstance(ast, MalList):
        out = []
        for i in ast.value:
            #print(str(i.value) + " MOREDUR")
            out.append(EVAL(i, env))
        return MalList(out)
    elif isinstance(ast, MalVector):
        out = []
        for i in ast.value:
            out.append(EVAL(i, env))
        return MalVector(out)
    else:
        #if(not ast):
         #   raise Exception("MURDER")
        print(str(ast) + " None found")
        if(isinstance(ast, MalType)):
            print(str(ast.value) + " found IS MAL")
        return ast


def is_pair(process):
    return isSeq(process) and len(process.value) > 0
    #else:
        #raise Exception("is_pair called on non list: {}".format(str(type(process))))

def quasiquote(process):

    if not is_pair(process):
        return MalList([MalSymbol("quote"),process])
    elif process.value[0].value == "unquote":
        return process.value[1]
    if(is_pair(process.value[0]) and (process.value[0].value[0].value == "splice-unquote")):
        return MalList([MalSymbol("concat"),process.value[0].value[1],quasiquote(MalList(process.value[1:]))])
    else:
        return MalList([MalSymbol("cons"), quasiquote(process.value[0]), quasiquote(MalList(process.value[1:]))])


def is_macro_call(ast, env : Env):
    out = False
    if(isList(ast)):
        if(isinstance(ast.value[0], MalSymbol)):
            if(env.find(ast.value[0])):
                if(hasattr(env.get(ast.value[0]), "isMacro")):
                    out = True
    return out

def macroexpand (ast, env : Env):
    while is_macro_call(ast, env):
        if(not isinstance(ast.value[0], MalSymbol)):
            raise Exception("MacroExpand first value in list non-symbol: {}".format(type(ast.value[0])))
        f = env.get(ast.value[0])
        ast = f(*ast.value[1:])
    return ast


def a1a2(ast):
    try:
        a1 = ast.value[1]
    except:
        a1 = Null
    try:
        a2 = ast.value[2]
    except:
        a2 = Null
    return a1,a2

def READ(process):
    return reader.read_str(process)
def EVAL(ast, env):
    while True:
        #(str(ast.value) + " DUMBSTICK")
        if(isinstance(ast, tuple)):
            raise Exception("TUPLE FOUND, KILL YOURSELF AND EVERYONE AROUND YOU")
        if not (isinstance(ast, MalList) or isinstance(ast, MalVector)):
            print("LISSS " + str(ast))
            return eval_ast(ast, env)
        elif ast.value == []:
            return ast
        else:
            print(ast.value)
           # print(str(type(ast.value[0])) + " TYME")
            #print(str(type(ast.value[1])) + " TYME2")

            ast = macroexpand(ast, env)

            if not (isinstance(ast, MalList) or isinstance(ast, MalVector)):
                print("LISSS " + str(ast))
                return eval_ast(ast, env)

            if(not isList(ast)):
                ast = eval_ast(ast, env)

            if(len(ast.value) == 0):
                return ast

            a0 = ast.value[0]
            print("dum " + str(a0))
            if(a0.value == "def!"):
                a1,a2 = a1a2(ast)
                print(str(a1)+ " I wanna die")
#                print("DEMMM " + printer.pr_str(EVAL(a2, env)))
                return env.seto(a1, EVAL(a2, env))
            elif(a0.value == "let*"):
                a1,a2 = a1a2(ast)
                nenv = Env(env)
                if (isinstance(a1, MalList)):
                    for i in range(0, int(len(a1.value)), 2):
                        if (isinstance(a1.value[i], str)):
                            raise Exception("Kaiba")
                        nenv.seto(a1.value[i], EVAL(a1.value[i + 1], nenv))
                ast = a2
                env = nenv
                #return EVAL(a2, nenv)
            elif(a0.value == "do"):
                #print("DOING")
                #return eval_ast(ast.value[1:], env)
                eval_ast(ast.value[1:-1], env)
                ast = ast.value[-1]

            elif (a0.value == "if"):
                a1,a2 = a1a2(ast)
                one = EVAL(a1, env)
                if (one != MalFalse and one != Null and one != False and one != None):
                    if(isinstance(one, MalType)):
                        if(one.value != None):
                            ast = a2
                    else:
                        if(isinstance(one, bool)):
                            ast = a2
                elif ((one == False or one == None or one == MalFalse) and len(ast.value) > 3):
                    print("HONK HONK !@$!@#(@&$#*^@")
                    if(len(ast.value) > 3):
                        ast = ast.value[3]
                    else:
                        ast = Null
                else:
                    ast = Null
            elif (a0.value == "defmacro!"):
                a1,a2 = a1a2(ast)
                f = EVAL(a2, env)
                f.isMacro = True
                print("Lookie!! " + str(f.isMacro))
                return env.seto(ast.value[1], f)
            elif (a0.value == "macroexpand"):
                ast = macroexpand(ast.value[1], env)
            elif (a0.value == "fn*"):
                a1,a2 = a1a2(ast)
                return MalFunction(EVAL,Env, a2,env,a1)
            elif (a0.value == "list"):
                print(str(a0)+ " PRESTOO")
                print(str(type(core.List(ast.value[1:]).value)) + " braking my bak")
                print(str(core.List(ast.value[1:])) + " this is the thing")
                return core.List(ast.value[1:])
            elif (a0.value == "quote"):
                a1,a2 = a1a2(ast)
                return a1
            elif (a0.value == "quasiquote"):
                ast = quasiquote(ast.value[1])
            elif "try*" == a0.value:
                if len(ast) < 3:
                    return EVAL(ast.value[1], env)
                a1, a2 = a1a2(ast)
                if a2.value[0] == "catch*":
                    err = None
                    try:
                        return EVAL(a1, env)
                    except MalException as exc:
                        err = exc.value
                    except Exception as exc:
                        err = exc.args[0]
                    catch_env = Env(env, [a2.value[1]], [err])
                    return EVAL(a2.value[2], catch_env)
                else:
                    return EVAL(a1, env)

            else:
                #print("OOOP " + str(ast.value[0].value) + " " + str(ast.value[1].value))
                process = eval_ast(ast, env)
                #print(str(process.value) +  " HWHUJW " + "OOOP " + str(ast.value[0].value) + " " + str(ast.value[1].value) + "    " + str(ast))
                #print(str(type(process.value[0])) + "  $%^&AWIND")
                #print(str(type(process.value[1])) + "  222222%^&2")
                print(str((process.value)) + "  1111111")
                print(str(type(process.value[0])))
                print(str(process.value[0]))

                while (isinstance(process.value[0], MalList)):
                    process = process.value[0]
                if (isinstance(process.value[0], list)):
                    oldprocess = process
                    process = panic(process)
                process = workarround(process, env)
                if(hasattr(process.value[0], "__ast__")):
                    ast = process.value[0].__ast__
                    env = process.value[0].__gen_env__(MalList(process.value[1:]))
                    pass
                else:
                    return process.value[0](*process.value[1:])
def PRINT(process):
    return printer.pr_str(process)
def repl(process):
    return PRINT(EVAL(READ(process), repl_env))


def panic(ast):
    if(isinstance(ast, MalList)):
        a = 0
        for i in ast.value:
            if(isinstance(i, list)):
                ast.value[a] = MalList(i)
                panic(i)
            a += 1
    return ast
def workarround(ast ,env):
    if(isinstance(ast, MalList)):
        if len(ast.value) == 1:
            if(isinstance(ast.value[0], MalList)):
                ast = ast.value[0]
                ast = workarround(ast, env)
                return eval_ast(ast, env)
        pos = 0
        for i in ast.value:
            if(isinstance(i, tuple)):
                if(len(i) == 1):
                    ast.value[pos] = i[0]
            pos += 1
    return ast


repl("(def! not (fn* (a) (if a false true)))")
repl("(def! load-file (fn* (f) (eval (read-string (str \"(do \" (slurp f) \")\")))))")
#repl("(def! sum2 (fn* (n acc) (if (= n 0) acc (sum2 (- n 1) (+ n acc)))))")

repl("(defmacro! cond (fn* (& xs) (if (> (count xs) 0) (list 'if (first xs) (if (> (count xs) 1) (nth xs 1) (throw \"odd number of forms to cond\")) (cons 'cond (rest (rest xs)))))))")
repl("(defmacro! or (fn* (& xs) (if (empty? xs) nil (if (= 1 (count xs)) (first xs) `(let* (or_FIXME ~(first xs)) (if or_FIXME or_FIXME (or ~@(rest xs))))))))")


while True:
    process = input()
    print(str(repl(process)) + " OUT")