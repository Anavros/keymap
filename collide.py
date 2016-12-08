
"""
Functions to measure key 'collisions'. A collision is when two keys are pressed
sequentially by the same finger, instead of being spread under two separate
fingers. This slows down typing and causes hand movement. Layouts should aim to
minimize collisions as per these metrics.
"""

import itertools


# Is this going to have a problem with reverse duplicates?
# e.g. 'ab' separate from 'ba'
def subset(chars, keycounts):
    """
    Check collisions between a small subset of characters.
    """
    collisions = {}
    for pair in itertools.permutations(chars, 2):
        pair = ''.join(pair)  # ('a', 'b') -> 'ab'
        try:
            occurance = keycounts[pair]
        except KeyError:
            continue
        else:
            collisions[pair] = occurance
    return collisions


def layout(keymap, keycounts):
    """
    Check collisions over an entire keyboard layout.
    """
    collisions = {}
    keys_by_finger = keymap.fingers()
    for finger, keylist in keys_by_finger.items():
        keyvalues = [k.value for k in keylist]
        # Only checks two-wide combinations; may change in future.
        for pair in itertools.permutations(keyvalues, 2):
            pair = ''.join(pair)  # from tuple to string
            if not pair.isalpha():
                continue
            try:
                occurance = keycounts[pair]
            except KeyError:
                continue
            else:
                collisions[pair] = occurance
    return collisions

