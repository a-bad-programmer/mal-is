from step3 import MalTypes

KEYWORD_PREFIX = 0x29E

def pr_str(mal, print_readably = True) -> str:
    print("TYPE " + str(type(mal)))
    print("WW " + str(mal))
    o = ""
    if isinstance(mal, MalTypes.MalSymbol):
        # print(mal.toString() + "   meee")
        return mal.toString()
    elif (isinstance(mal, int)):
        return str(mal)
    elif (isinstance(mal, str)):
        if(mal[0] == KEYWORD_PREFIX):
            return "keyword:" + mal[1:]
        print(mal + "AAAAAA")
        return '' + mal + ''
    elif (mal is MalTypes.MalBool):
        return str(mal.value())
    elif (isinstance(mal, MalTypes.MalList)):
        # print(mal.list())
        # print(o + " )))oooo")
        # print(mal.toString())
        o = ""
        for i in mal.list():
            if(isinstance(i, MalTypes.MalList)):
                o += pr_str(i)
            else:
                o += pr_str(i)
            o += ' '
        o = o[:-1]
        return '( ' + o + ' )'
    elif (isinstance(mal, MalTypes.MalVector)):
        # print(mal.list())
        # print(o + " )))oooo")
        # print(mal.toString())
        o = ""
        for i in mal.list():
            if(isinstance(i, MalTypes.MalVector)):
                o += pr_str(i)
            else:
                o += pr_str(i)
            o += ' '
        o = o[:-1]
        return '[ ' + o + ' ]'
    elif (isinstance(mal, MalTypes.MalInt)):
        return mal.toString()
    elif(mal is MalTypes.Null):
        return "Null"
    elif(callable(mal)):
       return "#<function>"
    else:
        type(mal)
        str(mal + "awdwaddwada")
