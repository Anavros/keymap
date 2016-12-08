

import argparse
import readline
import random
from layout import load


def generate(allowed):
    tasks = []
    for i in range(random.randint(2, 7)):
        random.shuffle(allowed)
        string = ''.join(allowed[:random.randint(1, len(allowed))])
        tasks.append(string)
    return ' '.join(tasks)


def loop(layout, allowed):
    while True:
        print('\n'*50)
        layout.print()
        print()
        task = generate(allowed)
        print(task)
        response = input()


def main(args):
    layout = load('/home/john/projects/keys/layouts/'+args.layout)
    try:
        loop(layout, list(args.allowed))
    except (EOFError, KeyboardInterrupt):
        print()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("layout", default='qwerty')
    parser.add_argument("-a", "--allowed", default='fj')
    main(parser.parse_args())
