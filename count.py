
import sys
import itertools
import argparse
from operator import itemgetter
from contextlib import contextmanager
from layout import Layout


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
            if ':' in combo or '"' in combo: continue
            x = keycounts.get(combo, 0)
            if x:
                colls[combo] = x
    return colls


def reactions(key, pairs):
    result = {}
    for chars, occurance in pairs.items():
        if key in chars:
            other = chars.replace(key, '')
            if not other: continue  # if pair is e.g. 'ee' and both are removed
            try:
                result[other] += occurance
            except KeyError:
                result[other] = occurance
    return result


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
    elif args.task == 'reactions':
        keycounts = ngraphs(args.file, 2, True)
        display(reactions(args.char, keycounts), args)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("task", default="count")
    parser.add_argument("file", nargs="?")
    parser.add_argument("-n", "--ngram", type=int, default=1)
    parser.add_argument("-l", "--layout", default='qwerty')
    parser.add_argument("-c", "--char", default='e')
    parser.add_argument("-m", "--minimum", type=int, default=0)
    parser.add_argument("-a", "--alpha", action='store_true')
    main(parser.parse_args())
