import sys
import argparse

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n')
    return parser

parser = createParser()
namespace = parser.parse_args(sys.argv[1:])

def Fibbonachi(a):
    a=int(a)
    if a == 1:
        return 0
    elif a == 2:
        return 1
    else:
        return (Fibbonachi(a-1) + Fibbonachi(a-2))

print(Fibbonachi(format(namespace.n)))