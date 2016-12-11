
import itertools
import argparse
from string import ascii_lowercase, punctuation

import layout
import collide
import display
import util


def ngrams(path, n, allowed=set()):
    count = {}
    with util.read_file_or_stdin(path) as f:
        while True:
            seq = f.read(n)
            if not seq:  # EOF
                break
            if ' ' in seq or '\n' in seq:  # not counting whitespace
                continue
            if allowed and not util.contained(seq, allowed):
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


def cost(layout, keycounts):
    result = {}
    for diff, keys in layout.difficulties().items():
        for k in keys:
            k = k.value
            try:
                result[k] = keycounts[k] * diff
            except KeyError:
                pass
    return result


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

# Is this going to have a problem with reverse duplicates?
# e.g. 'ab' separate from 'ba'
def subset_collisions(chars, keycounts):
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


def collisions(keymap, keycounts):
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
