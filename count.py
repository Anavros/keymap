
import sys
import itertools
import argparse
from operator import itemgetter
from contextlib import contextmanager
from layout import load as load_layout
from string import ascii_lowercase


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


# {'a': 100}, {'o': 100}
def balance(charcounts, layout):
    lkeys = {}
    rkeys = {}
    for c, n in charcounts.items():
        hand = layout.keys[c].finger[0]  # finger might be e.g. RI
        if hand == 'R':
            rkeys[c] = n
        elif hand == 'L':
            lkeys[c] = n
    return lkeys, rkeys


def fingers(charcounts, layout):
    # Iterate over finger->keylist mapping and change each keylist into a dict.
    fingers = {}
    for f, keys in layout.fingers().items():
        keydict = {}
        for k in keys:
            k = k.value
            try:
                count = charcounts[k]
            except KeyError:
                break
            keydict[k] = count
        fingers[f] = keydict
    return fingers


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


def complete(keycounts):
    """
    Take a {key: count} dictionary and fill in each key not already included
    with a default value of 0. Used for showing the absence of keys in a count.
    Creates a new dictionary to return.
    """
    new = {}
    for alpha in ascii_lowercase:
        try:
            count = keycounts[alpha]
        except KeyError:
            new[alpha] = 0
        else:
            new[alpha] = count
    return new


# TODO: docstrings for everything
# TODO: move tasks into separate functions and use dispatch dict
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
        actions = reactions(args.char, keycounts)
        actions = complete(actions)
        display(actions, args)

    elif args.task == 'fingers':
        layout = load_layout('/home/john/projects/keys/layouts/'+args.layout)
        keycounts = ngraphs(args.file, 1, False)
        for f, keys in sorted(fingers(keycounts, layout).items()):
            print(f)
            display(keys, args)

    elif args.task == 'balance':
        layout = load_layout('/home/john/projects/keys/layouts/'+args.layout)
        keycounts = ngraphs(args.file, 1, True)
        l, r = balance(keycounts, layout)
        print("Left:")
        display(l, args)
        print("Right:")
        display(r, args)


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
