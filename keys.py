
import itertools
import argparse
from string import ascii_lowercase, punctuation

import count
import balance
import layout
import collide
import display
import util
import strip


def get_keycounts(file, n=1, cached=False, alpha=False, punct=False):
    if cached:
        return util.uncache(file)
    else:
        if punct:
            allowed = set(punctuation)
        elif alpha:
            allowed = set(ascii_lowercase)
        else:
            allowed = set()
        return count.ngrams(file, n, allowed)


def main(args):
    keylayout = layout.load(args.layout)

    if args.task == 'count':
        keycounts = get_keycounts(args.file, args.n, args.cache, args.alpha, args.punct)
        util.display(keycounts, args.minimum, label="Key Counts:")

    elif args.task == 'collisions':
        bigrams = get_keycounts(args.file, 2, args.cache, alpha=True)
        if len(args.char) > 1:  # little hacky, default is 'e' so no bool check
            collisions = count.subset_collisions(args.char, bigrams)
        else:
            collisions = count.collisions(keylayout, bigrams)
        util.display(collisions, args.minimum)

    elif args.task == 'cost':
        unigrams = get_keycounts(args.file, 1, args.cache, alpha=True)
        costs = count.cost(keylayout, unigrams)
        util.display(costs, args.minimum)

    elif args.task == 'reactions':
        bigrams = get_keycounts(args.file, 2, args.cache, alpha=True)
        actions = count.reactions(args.char, bigrams)
        actions = util.complete(actions)
        display.columns(actions, args.minimum)

    elif args.task == 'fingers':
        unigrams = get_keycounts(args.file, 1, args.cache)
        for f, keys in sorted(balance.fingers(unigrams, keylayout).items()):
            print(f)
            util.display(keys, args.minimum)

    elif args.task == 'balance':
        unigrams = get_keycounts(args.file, 1, args.cache, alpha=True)
        l, r = balance.balance(unigrams, keylayout)
        util.display(l, args.minimum, label="Left:")
        util.display(r, args.minimum, label="Right:")

    elif args.task == 'hands':
        # Doesn't use caching!
        h = balance.hands(args.file, keylayout)
        util.display(h, args.minimum)

    elif args.task == 'minify':
        strip.minify(args.file)

    elif args.task == 'cache':
        keycounts = get_keycounts(args.file, args.n, False, args.alpha,
            args.punct)
        util.cache(keycounts)

    else:
        print("Unknown command: ", args.task)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("task", default="count")
    parser.add_argument("file", nargs="?")
    parser.add_argument("-n", type=int, default=1)
    parser.add_argument("-l", "--layout", default='qwerty')
    parser.add_argument("-c", "--char", default='e')
    parser.add_argument("-m", "--minimum", type=int, default=0)
    parser.add_argument("--alpha", action='store_true')
    parser.add_argument("--punct", action='store_true')
    parser.add_argument("--cache", action='store_true')
    main(parser.parse_args())
