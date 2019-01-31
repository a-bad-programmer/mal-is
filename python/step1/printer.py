from step1 import MalTypes


def pr_str(mal) -> str:
    # print("TYPE " + str(type(mal)))
    o = ""
    if isinstance(mal, MalTypes.Symbol):
        # print(mal.toString() + "   meee")
        return mal.toString()
    elif (isinstance(mal, int)):
        return str(mal)
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
        return '(' + o + ')'
    elif (isinstance(mal, MalTypes.MalInt)):
        return mal.toString()
    else:
        print("VERYBAD")
