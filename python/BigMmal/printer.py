from  BigMmal import MalTypes
def pr_str(process, readable = MalTypes.MalTrue):
    print(str(type(process)) + " POR")

    if(isinstance(process, MalTypes.MalSymbol) ):
        print(str(process) + "MEMEME")
        return process.value

    elif(isinstance(process, MalTypes.MalInt)):
        return str(process.value)

    elif(isinstance(process, MalTypes.MalList) or isinstance(process, MalTypes.MalVector)):
        out = ""
        for i in process.value:
            out += pr_str(i) + " "
        out = out[:-1]
        out = "(" + out + ")"
        return postCheck(out,readable)
    elif (isinstance(process, MalTypes.MalFunction)):
        return "<ƒuntion>"
    else:
        if(isinstance(process, int)):
            return pr_str(MalTypes.MalInt(process))
        print(str(type(process)) + " WOOPS")

def postCheck(input, readable):
    if(readable.value):
        input = input.replace("\"", "\\\"")
        input = input.replace("\\", '\\\\')
        input = input.replace("\n", "\\n")
    return input