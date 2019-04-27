import sys, re

def READ(x):
    return x

def EVAL(x):
    return x

def PRINT(x):
    return x

def rep(x):
    return READ(EVAL(PRINT(x)))

def repl():
    try:
        x = input()

        print(rep(x))
    except EOFError:
        exit()

while True:
    repl()