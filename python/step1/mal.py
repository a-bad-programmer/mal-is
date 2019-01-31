import sys, re

from step1 import reader, printer


def READ(x):
    return(reader.read_str(x))

def EVAL(x):
    return x

def PRINT(x):
    return printer.pr_str(x)

def rep(x):
    return PRINT(EVAL(READ(x)))

def repl():
    try:
        x = input()
        print(rep(x))
    except EOFError:
        exit()

while True:
    repl()
