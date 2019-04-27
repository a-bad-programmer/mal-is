from BigMmal.MalTypes import *
from BigMmal import Env, core

class Env():
    def __init__(self, outer:Env = Null, binds = EmptyList, exprs = EmptyList):
        self.outer = outer
        self.store = {}
        print(str(binds) + "HBB")
        for pos, i in enumerate(binds.value):
            if(binds.value[pos].value == "&"):
                self.seto(binds.value[pos + 1], exprs.value[pos:])
                break
            self.seto(i, exprs.value[pos])

    def seto(self, key:MalSymbol, value):
        #self.store[key] = value
        ret = False
        for i in self.store.keys():
            if(core.equals_(i, key)):
                self.store[i] = value
                ret = True
        if(not ret):
            self.store[key] = value
            i = key
        print(str(key) + " WHATHE")
        print(str(self.outer) + " WHY NO")
        print(str(value) + " vlue")
#        print(str(self.store[key]) + " 987654")
        print(" HERE " + str(self.store))
        return self.store[i]

    def find(self, key):
        tmpstore = []
        print("WOOO " + str(self.store) )
        print(self.store)
        for i in self.store:
            if(isinstance(i, str)):

                print(i)
                exit(1)
            tmpstore.append(i.value)
            print("searching: \"{}\" in {}".format(key.value, tmpstore))

        if key.value in tmpstore:
            return self
        elif self.outer != Null and self.outer != None:
            print("Pazzoozoo " + str(self.outer))
            return self.outer.find(key)
        else:
            print(key.value)
            return Null
            #raise Exception ("Key Not Found Error : Key {}".format(str(key.value)))


    def get(self, key):
        found_env = self.find(key)
        tmpstore = []
        if(found_env != Null):
            for i in found_env.store:
                print(i.value)
                if(i.value == key.value):
                    return found_env.store[i]
            return found_env.store[key]
        else:
            return found_env
