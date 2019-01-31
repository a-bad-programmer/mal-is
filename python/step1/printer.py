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
        return mal.toString()
    else:
        print("VERYBAD")
