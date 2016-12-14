
"""
Small, reusable utility functions to be used in other parts of the program.
"""

from sys import stdin
from contextlib import contextmanager
import operator
from string import ascii_lowercase


def contained(string, charset):
    """
    Does a string only contain characters from this set?
    """
    return set(string) < set(charset)


@contextmanager
def read_file_or_stdin(path):
    """
    Open a file object using a with block. If a filepath is given, open that
    file, and if not, return sys.stdin.
    """
    if path:
        f = open(path, 'r')
        yield f
        f.close()
    else:
        yield stdin


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


def display(keycounts, minimum, label=None):
    """
    Print data in columns and show a total at the end.
    """
    total = 0
    buffer = []
    if label: print(label)
    for c, n in sorted(keycounts.items(), key=operator.itemgetter(1)):
        if n >= minimum:
            buffer.append("'{}' {}".format(c, n))
        total += n
        if len(buffer) >= 3:
            print_row(buffer)
            buffer = []
    if buffer: print_row(buffer)
    print("Total:", total)


def print_row(strings):
    print(("{:<9} " * len(strings)).format(*strings))
