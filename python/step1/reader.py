import regex
from step1 import MalTypes
import step1.MalTypes

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
            return None
def read_list(reader:Reader):
    listo = []
    reader.next()
    token = reader.peek()
    print("STARR")
    while str(token) != ')':
        listo.append(read_form(reader))
        print(token)
        #input()
        token = reader.peek()
    reader.next()
    print(''.join(listo.__str__()))
    return MalTypes.MalList(listo)

def read_atom(reader:Reader):
    token = reader.next()
    #print(str(token) + "TOKEN")
    if(token.isnumeric()):
        return MalTypes.MalInt(int(token))
    else:
        return MalTypes.Symbol(token)
def tokenize(tokens:list):
    tokens = regex.split(r"[\s,]*(~@|[\[\]{}()'`~^@]|\"(?:\\.|[^\\\"])*\"?|;.*|[^\s\[\]{}('\"`,;)]*)", tokens)
    for i in tokens:
        if i == '':
            tokens.remove(i)
    print(tokens)
    return tokens
def read_str(string):
    return read_form(Reader(tokenize(string)))

def read_form(reader:Reader):
    token = reader.peek()
    if(token == '('):
        return read_list(reader)
    else:
        return read_atom(reader)

