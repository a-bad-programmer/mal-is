import re
from step1 import MalTypes
import step1.MalTypes

class Reader():
    def __init__(self, tokens):
        self.pos = 0
        self.tokens = tokens
    def next(self):
        self.pos += 1
        return self.tokens[self.pos - 1]

    def peak(self):
        if len(self.tokens) > self.pos:
            return self.tokens[self.pos]
        else:
            return None
def read_list(reader:Reader):
    list = MalTypes.MalList()
    reader.next()
    while True:
        c = read_form(reader)
        if c.string == ')':
            break
        list.add(c)
    return list

def read_atom(reader:Reader):
    token = reader.next()
    if(token.isnumeric()):
        return int(token)
    else:
        return MalTypes.Symbol(token)
def tokenize(tokens):
    re.split(r"[\s,]*(~@|[\[\]{}()'`~^@]|\"(?:\\.|[^\\\"])*\"?|;.*|[^\s\[\]{}('\"`,;)]*)", tokens)
    return tokens
def read_str(string):
    return read_form(Reader(tokenize(string)))

def read_form(reader:Reader):
    if(reader.peak() == '('):
        return read_list(reader)
    else:
        return read_atom(reader)