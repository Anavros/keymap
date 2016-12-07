
import sys
import itertools
import argparse
from operator import itemgetter


def ngraphs(path, n):
    count = {}
    if path:
        f = open(path, 'r')
    else:
        f = sys.stdin
    while True:
        di = f.read(n)
        if not di: break
        if ' ' in di or '\n' in di: continue
        try:
            count[di.lower()] += 1
        except KeyError:
            count[di.lower()] = 1
    f.close()
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
    parser.add_argument("file", nargs="?")
    parser.add_argument("-n", "--ngram", type=int, default=1)
    parser.add_argument("-c", "--collisions")
    main(parser.parse_args())
