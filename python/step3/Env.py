#from step3.MalTypes import MalSymbol
from step3 import MalTypes


class Env():

    def seto(self, symbol:MalTypes.MalSymbol, value):
        #print(symbol)
        if (isinstance(symbol, str)):
            symbol = MalTypes.MalSymbol(symbol)
            #raise Exception("Kaiba")
        self.data[symbol.value] = value
        #print("value " + str(value))
        #print("dumb " + str(self.data[symbol.value]) )
        return value
    def __init__(self, outer = None, binds = MalTypes.MalList(), exprs = MalTypes.MalList()):
        self.data = {}
        self.outer = outer
        i = 0
        #print("MURDER ++++ " + str(exprs.value))
        #print("MURDER ++ " + str(binds.value))
        #print("KIDIWNDNA" + str(binds.value))
        #print("&UFWUWFIH " + str(type(binds)))
        for item in (binds.value):
            #print("EYE" +str(i))
            #print("kill me " +str(exprs.value[i]))
            self.seto(item, exprs.value[i])
            i += 1

    def find(self, symbol:MalTypes.MalSymbol):
        if(symbol in self.data):
            return self.data
        else:
            if(self.outer != None):
                self.outer.find()
    def get(self, symbol:MalTypes.MalSymbol):
        env = self.find(symbol.value)
        if(env == None):
            raise Exception("Key Not Found Error")
        else:
            return env[symbol.value]
