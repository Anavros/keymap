
import sys
import itertools
import argparse
from operator import itemgetter


class Layout:
    def __init__(self, keylist):
        self.keys = [
            Key("A01", keylist[ 0], "LP", 1),  # q
            Key("A02", keylist[ 1], "LR", 1),  # w
            Key("A03", keylist[ 2], "LM", 1),  # e
            Key("A04", keylist[ 3], "LI", 1),  # r
            Key("A05", keylist[ 4], "LI", 1),  # t
            Key("A06", keylist[ 5], "RI", 1),  # y
            Key("A07", keylist[ 6], "RI", 1),  # u
            Key("A08", keylist[ 7], "RM", 1),  # i
            Key("A09", keylist[ 8], "RR", 1),  # o
            Key("A10", keylist[ 9], "RP", 1),  # p
            Key("A11", keylist[10], "RP", 1),  # [
            Key("A12", keylist[11], "RP", 1),  # ]
            Key("B01", keylist[12], "LP", 1),  # a
            Key("B02", keylist[13], "LR", 1),  # s
            Key("B03", keylist[14], "LM", 1),  # d
            Key("B04", keylist[15], "LI", 1),  # f
            Key("B05", keylist[16], "LI", 1),  # g
            Key("B06", keylist[17], "RI", 1),  # h
            Key("B07", keylist[18], "RI", 1),  # j
            Key("B08", keylist[19], "RM", 1),  # k
            Key("B09", keylist[20], "RR", 1),  # l
            Key("B10", keylist[21], "RP", 1),  # ;
            Key("B11", keylist[22], "RP", 1),  # '
            Key("C01", keylist[23], "LR", 1),  # z
            Key("C02", keylist[24], "LM", 1),  # x
            Key("C03", keylist[25], "LI", 1),  # c
            Key("C04", keylist[26], "LI", 1),  # v
            Key("C05", keylist[27], "RI", 1),  # b
            Key("C06", keylist[28], "RI", 1),  # n
            Key("C07", keylist[29], "RI", 1),  # m
            Key("C08", keylist[30], "RM", 1),  # ,
            Key("C09", keylist[31], "RR", 1),  # .
            Key("C10", keylist[32], "RP", 1),  # /
        ]

    def print(self):
        for key in self.keys:
            if key.position in ["B01", "C01"]: print()
            print(key.value, end=' ')
        print()

    def fingers(self):
        groups = {}
        for key in self.keys:
            try:
                groups[key.finger].append(key)
            except KeyError:
                groups[key.finger] = [key]
        return groups


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
        di = f.read(n)
        if not di: break
        if ' ' in di or '\n' in di: continue
        try:
            count[di.lower()] += 1
        except KeyError:
            count[di.lower()] = 1
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


def display(*counts):
    for count in counts:
        for c, n in sorted(count.items(), key=itemgetter(1)):
            print("'{}' {}".format(c, n))


def main(args):
    count = ngraphs(args.file, args.ngram)
    if args.test:
        layout = load_layout('/home/john/projects/keys/qwerty')
        colls = layout_collisions(layout, count, args.ngram)
        display(colls)
        return
    if args.collisions:
        colls = collisions(count, args.collisions, args.ngram)
        display(colls)
    else:
        display(count)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # TODO: set default file to be sys.stdin instead of None check in ngrams()
    parser.add_argument("file", nargs="?")
    parser.add_argument("-n", "--ngram", type=int, default=1)
    parser.add_argument("-c", "--collisions")
    parser.add_argument("-t", "--test", action='store_true')
    main(parser.parse_args())
