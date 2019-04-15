import regex
from BigMmal import MalTypes


KEYWORD_PREFIX = 0x29E


class Reader():
    def __init__(self, tokens, position = 0):
        self.tokens = tokens
        self.position = position
    def next(self):
        self.position += 1
        return self.tokens[self.position - 1]
    def peek(self):
        if(len(self.tokens) > self.position):
            return self.tokens[self.position]
        else:
            return None

def read_string(reader:Reader):
    token = MalTypes.MalString(reader.peek())
    token = token.replace("\\\"", "\"")
    token = token.replace("\\\\", '\\')
    token = token.replace("\\n", "\n")
    reader.next()
    return token

def read_atom(reader:Reader):
    token = reader.next()
    print(str(token) + "TOKEN")
    if(token.isnumeric()):
        return MalTypes.MalInt(int(token))
    elif (token == "true"):
        return MalTypes.MalBool(True)
    elif (token == "false"):
        return MalTypes.MalBool(False)
    elif (token == "nil"):
        return MalTypes.Null
    elif (token == ""):
        return MalTypes.Null
    elif (token == None):
        return MalTypes.Null
    else:
        print(token)
        return MalTypes.MalSymbol(token)


def read_list(reader:Reader):
    listo = []
    reader.next()
    token = reader.peek()
    while str(token) != ')':
        listo.append(read_form(reader))
        print(token)
        #input()
        token = reader.peek()
    reader.next()
    print(''.join(listo.__str__()) + 'LOSSSOO')
    return MalTypes.MalList(listo)
def read_vector(reader:Reader):
    listo = []
    reader.next()
    token = reader.peek()
    while str(token) != ']':
        listo.append(read_form(reader))
        print(token + "  TOKEN TOKEN TOKEN")
        #input()
        token = reader.peek()
    reader.next()
    print(''.join(listo.__str__()) + " LISTOO")
    return MalTypes.MalVector(listo)



def tokenize(in_tokens):
    tokens = regex.split(
        r"[\s,]*(~@|[\[\]{}()'`~^@]|\"(?:\\.|[^\\\"])*\"?|;.*|[^\s\[\]{}('\"`,;)]*)", in_tokens
    )
    for i in tokens:
        if i == '':
            tokens.remove(i)
        if len(i) > 0:
            if i[0] == ';':
                tokens.remove(i)
    print(tokens)
    return tokens
def read_str(string):
    return read_form(Reader(tokenize(string)))

def read_form(reader:Reader):
    token = reader.peek()
    if(token[0] == '('):
        return read_list(reader)
    elif(token[0] == '['):
        return read_vector(reader)
    elif(token[0] == '\"'):
        return read_string(reader)
    elif(token[0] == ':'):
        return KEYWORD_PREFIX + reader.next()[1:]
    else:
        return read_atom(reader)