import regex, re
from BigMmal import MalTypes, printer


KEYWORD_PREFIX = "\u029e"


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
            print("Something went wrong")
            return None

def read_string(reader:Reader):
    token = MalTypes.MalString(reader.peek())
    token.value = token.value[1:-1]
    print(token.value + "  WWOWOWOWOWW")
    token.value.replace("\\\"", "\"")
    token.value.replace("\\\\", '\\')
    token.value.replace("\\n", "\n")
    reader.next()
    return token

def read_atom(reader:Reader):
    token = reader.next()
    print(str(token) + "TOKEN")
    int_re = re.compile(r"-?[0-9][0-9.]*$")
    if re.match(int_re, token):
        return MalTypes.MalInt(int(token))
    elif (token == "true"):
        return MalTypes.MalTrue
    elif (token == "false"):
        return MalTypes.MalFalse
    elif (token == "nil"):
        return MalTypes.Null()
    elif (token == ""):
        print("BABDBAD")
        return MalTypes.Null()
    elif (token == None):
        print("NULL TOKEN PLEAWSE FIX")
        return MalTypes.Null()
    else:
        print(str(token) + " TOKENIZED")

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
    out = out2 = read_form(Reader(tokenize(string)))
    """while (isinstance(out2, MalTypes.MalList)):
        out2 = out2.value
        print(str(type(out)) + " DEADDEAD")
        tmp = ""
        for i in out2:
            if(isinstance(i, MalTypes.MalType)):
                tmp += str(i.value)
            else:
                tmp += str(i)
            tmp += " "
        print("TEMP " + tmp + " TEMP")
        print(str(out) + " OUT@")
        print(str(type(out)) + " O@T")
        out3 = out
        print(printer.pr_str(out))
    """
    if(isinstance(out, MalTypes.MalList)):
        print(str(out.value) + " OUT@2")
        #input("Continue...")

    return out

def read_hash_map(reader:Reader):
    listo = []
    reader.next()
    token = reader.peek()
    while str(token) != '}':
        listo.append(read_form(reader))
        print(token + "  TOKEN TOKEN TOKEN")
        #input()
        token = reader.peek()
    reader.next()
    print(''.join(listo.__str__()) + " LISTOO")
    return MalTypes.ezhash(listo)


def re_deref(reader:Reader):
    out = []
    out.append(MalTypes.MalSymbol("deref"))
    reader.next()
    out.append(read_form(reader))

def read_form(reader:Reader):
    token = reader.peek()
    if(token[0] == '('):
        return read_list(reader)
    elif(token[0] == '['):
        return read_vector(reader)
    elif(token[0] == '\"'):
        return read_string(reader)
    elif(token[0] == ':'):
        reader.next()
        return MalTypes.keywordify(token)
    elif(token[0] == '@'):
        return re_deref()
    elif (token[0] == "'"):
        reader.next()
        return MalTypes.MalList([MalTypes.MalSymbol("quote"), read_form(reader)])
    elif(token[0] == "`"):
        reader.next()
        return MalTypes.MalList([MalTypes.MalSymbol("quasiquote"), read_form(reader)])
    elif(token[0] == "~"):
        reader.next()
        return MalTypes.MalList([MalTypes.MalSymbol("unquote"), read_form(reader)])
    elif(token[0] == "~@"):
        reader.next()
        return MalTypes.MalList([MalTypes.MalSymbol("splice-unquote"), read_form(reader)])
    elif(token[0] == "{"):
        #reader.next()
        return read_hash_map(reader)
    else:
        return read_atom(reader)