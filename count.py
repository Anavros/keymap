
from sys import argv
from operator import itemgetter
from itertools import permutations
import argparse

# TODO: use stdin as input
# so you can cat 1 2 3 | kc
# TODO: format in columns

def digraphs(path):
    count = {}
    with open(path, 'r') as f:
        while True:
            di = f.read(2)
            if not di: break
            if ' ' in di or '\n' in di: continue
            try:
                count[di.lower()] += 1
            except KeyError:
                count[di.lower()] = 1
    return count


def ngraphs(path, n):
    count = {}
    with open(path, 'r') as f:
        while True:
            di = f.read(n)
            if not di: break
            if ' ' in di or '\n' in di: continue
            try:
                count[di.lower()] += 1
            except KeyError:
                count[di.lower()] = 1
    return count


def chars(path):
    count = {}
    with open(path, 'r') as f:
        while True:
            c = f.read(1)
            if not c: break
            if c in [' ', '\n']: continue
            try:
                count[c.lower()] += 1
            except KeyError:
                count[c.lower()] = 1
    return count


def collisions(count, keys):
    colls = {}
    for combo in permutations(keys):
        x = count.get(combo, 0)
        if x:
            colls[combo] = x
    return colls


def display(*counts):
    for count in counts:
        for c, n in sorted(count.items(), key=itemgetter(1)):
            print("'{}' {}".format(c, n))

def main(path):
    doubs = ngraphs(path, 2)
    colls = collisions(doubs, "nbjpmk")
    display(colls)


if __name__ == '__main__':
    assert len(argv) == 2, "Usage: {} <file>".format(argv[0])
    main(argv[1])
