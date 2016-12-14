

import argparse
import readline
import random

from constants import LAYOUTDIR
from layout import load

word_cache = []


def gibberish(allowed):
    random.shuffle(allowed)
    return ''.join(allowed[:random.randint(1, len(allowed))])


def dictionary():
    global word_cache
    return random.choice(word_cache)


def loop(layout, allowed):
    while True:
        print('\n'*50)
        print("Cache Length:", len(word_cache))
        layout.print()
        print()
        string = dictionary()
        print(string, string, string)
        response = input()


def load_word_cache(legal):
    global word_cache
    with open("/usr/share/dict/words", 'r') as f:
        for line in f:
            word = line.strip()
            if set(word.lower()) <= legal:
                word_cache.append(word)


def main(args):
    load_word_cache(set(args.allowed))
    layout = load(args.layout)
    try:
        loop(layout, list(args.allowed))
    except (EOFError, KeyboardInterrupt):
        print()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("layout", default='qwerty')
    parser.add_argument("-a", "--allowed", default='fj')
    main(parser.parse_args())
