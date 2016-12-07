
from sys import argv
from operator import itemgetter
import itertools
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


def collisions(count, keys, n):
    colls = {}
    for combo in itertools.permutations(keys, n):
        combo = ''.join(combo)  # should be string, not tuple
        x = count.get(combo, 0)
        if x: colls[combo] = x
    return colls


def display(*counts):
    for count in counts:
        for c, n in sorted(count.items(), key=itemgetter(1)):
            print("'{}' {}".format(c, n))


def main(args):
    count = ngraphs(args.file, args.ngram)
    if args.collisions:
        colls = collisions(count, args.collisions, args.ngram)
        display(colls)
    else:
        display(count)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file", default=None)
    parser.add_argument("-n", "--ngram", type=int, default=1)
    parser.add_argument("-c", "--collisions")
    main(parser.parse_args())
