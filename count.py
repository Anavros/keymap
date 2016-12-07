
import sys
import itertools
import argparse
from operator import itemgetter
from contextlib import contextmanager


class Layout:
    def __init__(self, positions, keys, fingers, costs):
        self.keys = { k:Key(p,k,f,int(c)) for p,k,f,c in
            zip(positions, keys, fingers, costs) }

    def print(self):
        for key in self.keys.values():
            if key.position in ["B01", "C01"]: print()
            print(key.value, end=' ')
        print()

    def _group(self, keyfunc):
        groups = {}
        for key in self.keys.values():
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


def load_layout(
        keypath,
        costpath='/home/john/projects/keys/cost',
        fingerpath='/home/john/projects/keys/finger',
        positionpath='/home/john/projects/keys/position',
    ):
    with open(positionpath, 'r') as f:
        positionlist = f.read().split()
    with open(keypath, 'r') as f:
        keylist = f.read().split()
    with open(fingerpath, 'r') as f:
        fingerlist = f.read().split()
    with open(costpath, 'r') as f:
        costlist = f.read().split()
    return Layout(positionlist, keylist, fingerlist, costlist)


@contextmanager
def read_file_or_stdin(path):
    if path:
        f = open(path, 'r')
        yield f
        f.close()
    else:
        yield sys.stdin


def ngraphs(path, n, alpha):
    count = {}
    with read_file_or_stdin(path) as f:
        while True:
            seq = f.read(n)
            if not seq:  # EOF
                break
            if ' ' in seq or '\n' in seq:  # not counting whitespace
                continue
            if alpha and not seq.isalpha():
                continue
            seq.replace(';', ':')
            seq.replace('\'', '\"')
            char = seq.lower()
            try:
                count[char] += 1
            except KeyError:
                try:
                    count[char[::-1]] += 1
                except KeyError:
                    count[char] = 1
    return count


def hands(path, layout):
    keys = layout.keys
    string = ''
    strings = {}
    on_hand = 'L'
    def add():
        nonlocal string, strings
        if len(string) < 3: return
        try:
            strings[string] += 1
        except KeyError:
            strings[string] = 1
        string = ''

    with read_file_or_stdin(path) as f:
        while True:
            c = f.read(1)
            if not c: break
            try:
                hand = keys[c].finger[0]
            except KeyError:
                add()
                continue
            if hand == on_hand:
                string += c
            else:
                on_hand = hand
                add()
    return strings


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
        display(ngraphs(args.file, args.ngram, args.alpha), args)
    elif args.task == 'collisions':
        layout = load_layout('/home/john/projects/keys/layouts/'+args.layout)
        keycounts = ngraphs(args.file, 2, args.alpha)
        display(layout_collisions(layout, keycounts, 2), args)
    elif args.task == 'cost':
        layout = load_layout('/home/john/projects/keys/layouts/'+args.layout)
        keycounts = ngraphs(args.file, 1, args.alpha)
        display(ease(layout, keycounts), args)
    elif args.task == 'hands':
        layout = load_layout('/home/john/projects/keys/layouts/'+args.layout)
        display(hands(args.file, layout), args)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("task", default="count")
    parser.add_argument("file", nargs="?")
    parser.add_argument("-n", "--ngram", type=int, default=1)
    parser.add_argument("-l", "--layout", default='qwerty')
    parser.add_argument("-c", "--collisions")
    parser.add_argument("-m", "--minimum", type=int, default=0)
    parser.add_argument("-a", "--alpha", action='store_true')
    main(parser.parse_args())
