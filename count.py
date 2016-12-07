
import sys
import itertools
import argparse
from operator import itemgetter


class Layout:
    def __init__(self, keylist):
        self.keys = [
            Key("A01", keylist[ 0], "LP", 2),  # q
            Key("A02", keylist[ 1], "LR", 2),  # w
            Key("A03", keylist[ 2], "LM", 2),  # e
            Key("A04", keylist[ 3], "LI", 3),  # r
            Key("A05", keylist[ 4], "LI", 4),  # t
            Key("A06", keylist[ 5], "RI", 4),  # y
            Key("A07", keylist[ 6], "RI", 3),  # u
            Key("A08", keylist[ 7], "RM", 2),  # i
            Key("A09", keylist[ 8], "RR", 2),  # o
            Key("A10", keylist[ 9], "RP", 2),  # p
            Key("B01", keylist[10], "LP", 1),  # a
            Key("B02", keylist[11], "LR", 1),  # s
            Key("B03", keylist[12], "LM", 1),  # d
            Key("B04", keylist[13], "LI", 1),  # f
            Key("B05", keylist[14], "LI", 3),  # g
            Key("B06", keylist[15], "RI", 3),  # h
            Key("B07", keylist[16], "RI", 1),  # j
            Key("B08", keylist[17], "RM", 1),  # k
            Key("B09", keylist[18], "RR", 1),  # l
            Key("B10", keylist[19], "RP", 1),  # :
            Key("B11", keylist[20], "RP", 4),  # "
            Key("C01", keylist[21], "LR", 5),  # z
            Key("C02", keylist[22], "LM", 5),  # x
            Key("C03", keylist[23], "LI", 3),  # c
            Key("C04", keylist[24], "LI", 4),  # v
            Key("C05", keylist[25], "RI", 5),  # b
            Key("C06", keylist[26], "RI", 4),  # n
            Key("C07", keylist[27], "RI", 3),  # m
        ]

    def print(self):
        for key in self.keys:
            if key.position in ["B01", "C01"]: print()
            print(key.value, end=' ')
        print()

    def _group(self, keyfunc):
        groups = {}
        for key in self.keys:
            try:
                groups[keyfunc(key)].append(key)
            except KeyError:
                groups[keyfunc(key)] = [key]
        return groups

    def fingers(self):
        return self._group(lambda k: k.finger)

    def difficulties(self):
        return self._group(lambda k: k.ease)


class Key:
    def __init__(self, position, value, finger, ease):
        self.position = position
        self.value = value
        self.finger = finger
        self.ease = ease

    def __repr__(self):
        return self.value


def load_layout(path):
    with open(path, 'r') as f:
        keylist = f.read().split()
    return Layout(keylist)


def ngraphs(path, n):
    count = {}
    if path:
        f = open(path, 'r')
    else:
        f = sys.stdin
    while True:
        seq = f.read(n)
        if not seq:  # EOF
            break
        if ' ' in seq or '\n' in seq:  # not counting whitespace
            continue
        seq.replace(';', ':')
        seq.replace('\'', '\"')
        char = seq.lower()
        try:
            count[char] += 1
        except KeyError:
            count[char] = 1
    f.close()
    return count


def collisions(count, keylist, n):
    colls = {}
    for keyset in keylist.split():  # space-separated
        for combo in itertools.permutations(keyset, n):
            combo = ''.join(combo)  # should be string, not tuple
            x = count.get(combo, 0)
            if x: colls[combo] = x
    return colls


def layout_collisions(layout, keycounts, n):
    colls = {}
    for keys in layout.fingers().values():
        for combo in itertools.permutations((k.value for k in keys), n):
            combo = ''.join(combo)  # should be string, not tuple
            x = keycounts.get(combo, 0)
            if x: colls[combo] = x
    return colls


def ease(layout, keycounts):
    cost = {}
    for diff, keys in layout.difficulties().items():
        for k in keys:
            k = k.value
            try:
                cost[k] = keycounts[k] * diff
            except KeyError:
                pass
    return cost


def display(count, args):
    total = 0
    for c, n in sorted(count.items(), key=itemgetter(1)):
        total += n
        if args.minimum and n < args.minimum:
            pass
        else:
            print("'{}' {}".format(c, n))
    print("Total:", total)


def main(args):
    if args.task == 'count':
        display(ngraphs(args.file, args.ngram), args)
    elif args.task == 'collisions':
        layout = load_layout('/home/john/projects/keys/layouts/'+args.layout)
        keycounts = ngraphs(args.file, 2)
        display(layout_collisions(layout, keycounts, 2), args)
    elif args.task == 'cost':
        layout = load_layout('/home/john/projects/keys/layouts/'+args.layout)
        keycounts = ngraphs(args.file, 1)
        display(ease(layout, keycounts), args)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("task", default="count")
    parser.add_argument("file", nargs="?")
    parser.add_argument("-n", "--ngram", type=int, default=1)
    parser.add_argument("-l", "--layout", default='qwerty')
    parser.add_argument("-c", "--collisions")
    parser.add_argument("-m", "--minimum", type=int, default=0)
    main(parser.parse_args())
