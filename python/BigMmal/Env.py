from BigMmal.MalTypes import *
from BigMmal import Env

class Env():
    def __init__(self, outer:Env = Null, binds = EmptyList, exprs = EmptyList):
        self.outer = outer
        self.store = {}
        print(str(binds) + "HBB")
        for pos, i in enumerate(binds.value):
            if(binds[pos].value == "&"):
                self.seto(binds[pos + 1], exprs[pos:])
                break
            self.seto(i, exprs.value[pos])

    def seto(self, key:MalSymbol, value):
        self.store[key] = value
        return self.store[key]

    def find(self, key):
        tmpstore = []
        for i in self.store:
            if(isinstance(i, str)):
                print(i)
                exit(1)
            tmpstore.append(i.value)
        if key.value in tmpstore:
            return self
        elif self.outer != Null and self.outer != None:
            return self.outer.find(key)
        else:
            print(key.value)
            raise Exception ("Key Not Found Error : Key {}".format(str(key.value)))


    def get(self, key):
        found_env = self.find(key)
        tmpstore = []
        for i in found_env.store:
            print(i.value)
            if(i.value == key.value):
                return found_env.store[i]
        return found_env.store[key]

