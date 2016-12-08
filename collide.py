
"""
Functions to measure key 'collisions'. A collision is when two keys are pressed
sequentially by the same finger, instead of being spread under two separate
fingers. This slows down typing and causes hand movement. Layouts should aim to
minimize collisions as per these metrics.
"""

import itertools


# Is this going to have a problem with reverse duplicates?
# e.g. 'ab' separate from 'ba'
def subset(keycounts, chars):
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


# TODO: Clean up, swap arguments.
def layout(keymap, counts):
    """
    Check collisions over an entire keyboard layout.
    """
    colls = {}
    for keys in keymap.fingers().values():
        # Only checks two-wide combinations; may change in future.
        for combo in itertools.permutations((k.value for k in keys), 2):
            combo = ''.join(combo)  # should be string, not tuple
            if ':' in combo or '"' in combo: continue
            x = counts.get(combo, 0)
            if x:
                colls[combo] = x
    return colls

