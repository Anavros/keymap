
"""
Functions for outputting keycount data in an easy-to-read way.
"""

import operator


def columns(keycounts, minimum, label=None):
    """
    Print data in columns and show a total at the end.
    """
    total = 0
    buffer = []
    if label: print(label)
    for c, n in sorted(keycounts.items(), key=operator.itemgetter(1)):
        if n > minimum:
            buffer.append("'{}' {}".format(c, n))
        total += n
        if len(buffer) >= 3:
            print_row(buffer)
            buffer = []
    print_row(buffer)
    print("Total:", total)


def print_row(strings):
    print(("{:>9} " * len(strings)).format(*strings))
