from  BigMmal import MalTypes
def pr_str(process, readable = None):
    print(str(type(process)) + " POR")
    if(readable is None):
        readable = MalTypes.MalBool(True)
    if(isinstance(process, MalTypes.MalSymbol) ):
        print(str(process) + "MEMEME")
        return process.value

    elif(isinstance(process, MalTypes.MalInt)):
        return str(process.value)

    elif(type(process) == type(MalTypes.Null)):
        return "nil"

    elif(isinstance(process, MalTypes.MalList) or isinstance(process, MalTypes.MalVector)):
        out = ""
        for i in process.value:
            out += pr_str(i, readable) + " "
        out = out[:-1]
        out = "(" + out + ")"
        return out
    elif isinstance(process, MalTypes.MalBool):
        return str(process.value)
    elif (isinstance(process, MalTypes.MalFunction)):
        return "<ƒuntion>"
    elif (isinstance(process, MalTypes.MalString)):
        if(process.value[0] == "\u029e"):
            process.value[0] = ":"
        return "" + pr_str(process.value, MalTypes.MalFalse) + ""
    elif (isinstance(process, MalTypes.Atom)):
        return "ATOM({})".format(pr_str(process.value))
    elif (isinstance(process, str)):
        return postCheck(process, readable.value)
    elif (MalTypes.isMap(process)):
        out = ""
        for i in process.value:
            out += "( " + pr_str(i, readable) + ", " + pr_str(process.value[i], readable) + " )"

        out = "{" + out + "}"
        return out
    else:
        if(isinstance(process, int)):
            return pr_str(MalTypes.MalInt(process))
        print(str(type(process)) + " WOOPS")
        """if(isinstance(process, list)):
            print("BIG DUMB")
            return pr_str(MalTypes.MalList(process))"""

def postCheck(input, readable):
    if(bool(readable)):
        input = input.replace("\"", "\\\"")
        input = input.replace("\\", '\\\\')
        input = input.replace("\n", "\\n")
    print(bool(readable))
    #print(readable.value)
    return input