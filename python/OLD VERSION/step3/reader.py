import regex
from step3 import MalTypes

KEYWORD_PREFIX = 0x29E

class Reader():
    def __init__(self, tokens):
        self.pos = 0
        self.tokens = tokens
    def next(self):
        self.pos += 1
        #print(self.tokens)
        #print(self.pos)
        return self.tokens[self.pos - 1]

    def peek(self):
        if len(self.tokens) > self.pos:
            return self.tokens[self.pos]
        else:
            print("OH GOD EVERYTHING IS ON FIRE")
            return MalTypes.Null

def read_string(reader:Reader):
    token = MalTypes.MalString(reader.peek())
    token = token.replace("\\\"", "\"")
    token = token.replace("\\\\", '\\')
    token = token.replace("\\n", "\n")
    reader.next()
    return token

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

def read_atom(reader:Reader):
    token = reader.next()
    print(str(token) + "TOKEN")
    if(token.isnumeric()):
        return MalTypes.MalInt(int(token))
    elif (token == "true"):
        return True
    elif (token == "false"):
        return False
    elif (token == "nil"):
        return None
    elif (token == ""):
        return None
    else:
        return MalTypes.MalSymbol(token)





def tokenize(tokens:list):
    tokens = regex.split(r"[\s,]*(~@|[\[\]{}()'`~^@]|\"(?:\\.|[^\\\"])*\"?|;.*|[^\s\[\]{}('\"`,;)]*)", tokens)
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


